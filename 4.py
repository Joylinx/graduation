import cv2
import numpy as np

piclist=[]

img = cv2.imread('D:/study/python program/7.jpg')
    #print(img.size) # 像素总数目
    #print(img.dtype)
    #print(img)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
pic=np.array(img)
pic_hsv=np.array(hsv)
m=pic_hsv.shape[0]
n=pic_hsv.shape[1]

print(m)
print(n)

H=0
S=0
V=0

for i in range(0,m):
    for j in range(0,n):
            H=H+(pic_hsv[i,j,0]/(n*m))
            S=S+(pic_hsv[i,j,1]/(n*m))
            V=V+(pic_hsv[i,j,2]/(n*m))



print(H)
print(S)
print(V)
