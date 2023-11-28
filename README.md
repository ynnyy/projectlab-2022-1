# yn0212.github.io
# 웹 기반 imu 센서를 이용한 사용자 상태 모니터링 시스템
project Lab [MQTT + Node_Red]
# 개요
MQTT와 Node_Red를 기반으로 만들어진 웹페이지에 rp2040 imu센서의 값을 출력해주는 프로젝트입니다.


# 블록도
![image](https://user-images.githubusercontent.com/105347300/174740546-2e55374d-3c6e-43d8-a3f7-2b173625ded7.png)

# 과제 내용
rp2040에 달려있는 imu센서를 통해 사용자가 움직이는 가속도 값을 받아와 평균값을 구함.
구한 평균값으로 사용자의 상태를 판별해 run,walk,stand를 Node_Red에 chart 와 text로 출력.
# 구현 영상


https://user-images.githubusercontent.com/105347300/175266328-edfd8d5e-f90c-45ec-bb01-faf4845abcb4.mp4



