import cv2

# 创建VideoCapture对象，打开摄像头
cap = cv2.VideoCapture(0)

# 定义BackgroundSubtractor对象，用于背景减除
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

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

    for contour in contours:
        # 计算轮廓的面积
        area = cv2.contourArea(contour)

        # 根据面积阈值判断是否为运动物体
        if area > 800:
            # 在原图上绘制矩形框
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示原图和处理后的图像
    cv2.imshow("Original", frame)
    # cv2.imshow("Foreground", fg_mask)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
