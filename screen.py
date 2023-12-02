# 显示器模块
# coding=utf-8
# !/usr/bin/env python3
# created by xieyuheng
import LCD1602
import time

def screen_setup():
    # 显示器启动
    LCD1602.init(0x27,1)
    LCD1602.write(0,0,'System Booting!')
    LCD1602.write(0,1,'Author: XYH , LY')
    time.sleep(1)
    LCD1602.clear()
    pass

# 根据红外信号调整不同的显示
def screen_show(chose,light,humidity,temperature,if_rained,humi_temp_warning):
    LCD1602.clear()
    print(1)
    # 1->光强，下雨；2->温湿度
    if humi_temp_warning == 0:
        # print(f"no warning\tchose:{chose}")
        if chose == 1:
            if if_rained:
                rain_str = "IF_RAIN: raining"
                pass
            else:
                rain_str = "IF_RAIN: sunny"
            LCD1602.write(0,0,rain_str)
            LCD1602.write(0,1,f"LIGHT: {light}")
        elif chose == 2:
            LCD1602.write(0,0,f"TEMP: {temperature}")
            LCD1602.write(0,1,f"HUMI: {humidity}%")
        pass
    else:
        if humi_temp_warning == 1:
            print(f"HUMI:{humidity}")
            LCD1602.write(0,0,"Warning!!!!")
            LCD1602.write(0,1,"HUMI is too high!")
            pass
        else:
            print(f"TEMP:{temperature}")
            LCD1602.write(0,0,"Warning!!!!")
            LCD1602.write(0,1,"TEMP is too high!")
            pass
        pass
    time.sleep(0.2)