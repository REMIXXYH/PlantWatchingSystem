# 温湿度获取模块
# coding=utf-8
# !/usr/bin/env python3
# created by xieyuheng
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT

makerobo_pin = 12
makerobo_Rpin_d= 36   #红色LEDPin端口
makerobo_Gpin_d= 33   #绿色LEDPin端口

# 双色灯初始化
def color2_LED_setup():
    GPIO.setmode(GPIO.BOARD) #采用实际的物理管脚给GPIO口
    GPIO.setwarnings(False)  #去除GPIO口警告
    GPIO.setup(makerobo_Rpin_d,GPIO.OUT)  #设置红色LED管脚为输出模式
    GPIO.setup(makerobo_Gpin_d,GPIO.OUT)  #设置绿色LED管脚为输出模式

# 双色灯颜色切换
def LED2_switch(x):
    if x:  #x为1时,开启绿色LED灯
        GPIO.output( makerobo_Rpin_d,0)
        GPIO.output( makerobo_Gpin_d,1)
    else:  #x为0时,开启红色LED灯
        GPIO.output( makerobo_Rpin_d,1)
        GPIO.output( makerobo_Gpin_d,0)

# 获取温湿度
def get_humi_temp():
    humidity, temperature = DHT.read_retry(11, makerobo_pin)
    return humidity,temperature

# 控制温湿度报警灯
def humi_temp_warning(humidity, temperature):
    # 温度或湿度超标
    if humidity >=55:
        LED2_switch(0)
        return 1 # 湿度超标返回
    elif temperature >= 35:
        LED2_switch(0)
        return 2 # 温度超标返回
    else:
        LED2_switch(1)
        return 0
