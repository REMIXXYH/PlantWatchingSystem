# 无源蜂鸣器模块
# coding=utf-8
# !/usr/bin/env python3
# created by xieyuheng
import RPi.GPIO as GPIO

makerobo_Buzzer = 11 # 有源蜂鸣器管脚定义

# 蜂鸣器初始化
def Buzzer_setup():
    global makerobo_BuzzerPin
    makerobo_BuzzerPin = makerobo_Buzzer
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(makerobo_BuzzerPin, GPIO.OUT)
    GPIO.output(makerobo_BuzzerPin, GPIO.HIGH)

# 打开蜂鸣器
def buzzer_on():
    GPIO.output(makerobo_BuzzerPin, GPIO.LOW)  # 蜂鸣器为低电平触发，所以使能蜂鸣器让其发声

# 关闭蜂鸣器
def buzzer_off():
    GPIO.output(makerobo_BuzzerPin, GPIO.HIGH) # 蜂鸣器设置为高电平，关闭蜂鸟器

def destroy():
    GPIO.output(makerobo_BuzzerPin, GPIO.HIGH) # 关闭蜂鸣器鸣叫 释放资源
    GPIO.cleanup()