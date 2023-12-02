# 主函数 
# coding=utf-8
# !/usr/bin/env python3
# created by xieyuheng

import cv2
import threading
# 自定义模块
import humiture_my
import PCF8591_using
import screen
import red_remote_control
import Buzzer

# 创建互斥锁
lock = threading.Lock()

# 基础数值监测
def Basic_Statistics_Watching():
    # 设置液晶屏显示默认值
    chose = 2
    # try:
    while True:
        humidity,temperature = humiture_my.get_humi_temp()
        warning=humiture_my.humi_temp_warning(humidity, temperature)
        if_rain = PCF8591_using.get_if_rained()
        lighting = PCF8591_using.get_lighting()
        PCF8591_using.Control_Sim_Lighting(lighting)
        red_flag = red_remote_control.get_show_chosen()
        if red_flag is None:
            screen.screen_show(chose,lighting,humidity,temperature,if_rain,warning)
        else:
            chose = red_flag
            pass
        pass
        # 释放锁
        if lock.locked():
            lock.release()
            pass
        pass
    # except:
    #     print("Basic Statistics Watching Module Run Wrong!")


# 动捕模块
def Dynamic_Object_Watching():
    # 创建VideoCapture对象，打开摄像头
    cap = cv2.VideoCapture(0)
    # 定义BackgroundSubtractor对象，用于背景减除
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()
    try:
        while True:
            # 读取视频帧
            ret, frame = cap.read()
            if not ret:
                break
            # 对当前帧应用背景减除器
            fg_mask = bg_subtractor.apply(frame)
            # 对前景掩码进行处理，如去除噪声、进行形态学操作等
            # 寻找轮廓
            contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            Buzzer.buzzer_off()
            for contour in contours:
                # 计算轮廓的面积
                area = cv2.contourArea(contour)
                # 根据面积阈值判断是否为运动物体
                if area > 800:
                    # 在原图上绘制矩形框
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    Buzzer.buzzer_on()
                    break
            # 显示原图和处理后的图像
            cv2.imshow("Original", frame)
            # 按下'q'键退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            pass
            # 释放锁
            if lock.locked():
                lock.release()
        pass
    except:
        print("Dynamic Module Run Wrong!")

# 系统主函数
if __name__ == '__main__':
    # 初始化PCF8591
    PCF8591_using.PCF_set_up()
    # 初始化双色灯
    humiture_my.color2_LED_setup()
    # 初始化显示屏
    screen.screen_setup()
    # 初始化红外线
    red_remote_control.red_control_setup()
    # 初始化蜂鸣器
    Buzzer.Buzzer_setup()

    try:
        # 创建线程对象
        thread1 = threading.Thread(target=Basic_Statistics_Watching, name="Thread_1")
        thread2 = threading.Thread(target=Dynamic_Object_Watching,   name="Thread_2")
        # 启动线程
        thread1.start()
        thread2.start()
        # 等待线程结束
        thread1.join()
        thread2.join()
        pass
    except:
        print("System Shutdown!!!")
