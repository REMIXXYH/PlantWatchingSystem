# 此模块用于使用PCF8591的部分
# coding=utf-8
# !/usr/bin/env python3
# created by xieyuheng

import PCF8591 as ADC
import time

def PCF_set_up():
    ADC.setup(0x48)
    pass

def get_if_rained():
    # AIN1作为雨滴输入
    rain = ADC.read(1)
    if (rain <= 180):
        return 1
    else:
        return 0

# 返回光照强度
def get_lighting():
    # 获取光敏电阻
    lighting = 255-int(ADC.read(0))
    if  lighting > 200:
        return "High"
    elif lighting > 120 and lighting <=200:
        return "Medium"
    elif lighting <= 120:
        return "Low"

# 光强控制三色灯给光
def Control_Sim_Lighting(status):
    hour = time.localtime().tm_hour
    # 只有白天且光照强度不够时才人工给光
    if hour>=6 and hour <= 23 and status == "Low":
        ADC.write(200)
    else:
        ADC.write(0)