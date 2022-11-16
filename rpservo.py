import network,time
from lsm6dsox import LSM6DSOX
from simple import MQTTClient
from machine import I2C,Pin,Timer

import random
import time
import paho.mqtt.client as mqtt_client
import RPi.GPIO as GPIO                     # 
import time                                 # 
from pymata4 import pymata4
import sys
lsm = LSM6DSOX(I2C(0, scl=Pin(13), sda=Pin(12)))
step1 = 0
board = pymata4.Pymata4()
servo = board.set_pin_mode_servo(11) # 


def move_servo(v):                  # 
    board.servo_write(11, v)
    time.sleep(1) 
    
def WIFI_Connect():
    wlan = network.WLAN(network.STA_IF) #STA模式
    wlan.active(True)                   #激活接口
    start_time=time.time()              #记录时间做超时判断

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ncs', '12312300') #输入WIFI账号密码
        
    if wlan.isconnected():
        print('network information:', wlan.ifconfig())
        return True    

def MQTT_Send(tim):
    global step1
    step1 = step1 +1
    a = lsm.read_accel()
    print('Accelerometer: x:{:>8.3f} y:{:>8.3f} z:{:>8.3f}'.format(*lsm.read_accel()))
    if((a[0] >= -0.07 and a[0] <=0.12) and( a[1]<= 0.020 and a[1] >= -0.025) and (a[2] <= 1.02 and a[2] >= 1.0)):
        client.publish(TOPIC, "He is standing")
        move_servo(90)
    elif((a[0] >= -0.4 and a[0] <=3) and( a[1]>= -0.5 and a[1] <=2.5) and (a[2] >= -2 and a[2] <=3)):
        client.publish(TOPIC, "He is walking")
        move_servo(30)
    else:
        client.publish(TOPIC, "He is running")
        move_servo(0)
    time.sleep_ms(1000)
    print(step1)
if WIFI_Connect():
    SERVER = '192.168.0.78'
    PORT = 1883
    CLIENT_ID = 'pi' # clinet id 이름
    TOPIC = 'rp2040' # TOPIC 이름
    client = MQTTClient(CLIENT_ID, SERVER, PORT,keepalive=30)
    client.connect()

    #开启RTOS定时器，编号为-1,周期1000ms，执行socket通信接收任务
    tim = Timer(-1)
    tim.init(period=1000, mode=Timer.PERIODIC,callback=MQTT_Send)




