# 红外遥控模块
# coding=utf-8
# !/usr/bin/env python3
# created by xieyuheng

import pylirc
import smbus
bus=smbus.SMBus(1)
blocking = 0

# 红外遥控初始化
def red_control_setup():
    # 遥控器启动
    pylirc.init("pylirc","/etc/lirc/conf",blocking)
    pass

# 按键对应信号译码
def switch_show(config):
    if config == "KEY_CHANNELDOWN": # 第一行第一个按键显示温度是否下雨和光强
        return 1
    elif config == "KEY_CHANNEL":
        return 2
    return 0

# 获取红外信号序列
def get_show_chosen():
    # 红外线指示
    s = pylirc.nextcode(1)
    while(s):
        for (code) in s:
            print("Command: ",code["config"])
            # 选择显示内容
            return switch_show(code["config"])