import cv2
import numpy as np

img = cv2.imread("D:/study/python program/zlx/1/3.jpg", 1)
cv2.namedWindow('src', 0)
cv2.imshow("src", img)

# 彩色图像均衡化,需要分解通道 对每一个通道均衡化
(b, g, r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# 合并每一个通道
result = cv2.merge((bH, gH, rH))

cv2.namedWindow('dst', 0)
cv2.imshow("dst", result)

cv2.waitKey(0)