import cv2
import numpy as np


#需要修改的参数：图片位置及名称，图片数量，筛选背景的初始设定值

#自定义函数：
#把区域为[min, max]的分布，按间隔为1划成max-min份, 并分配从外部输入数据在此区间的分布,并将结果输出到n数组中
def frequent(min,max,x,n):
	#n=np.linspace(0, 0, max-min)
	for i in range(min, max):
		if (x>=i and x<i+1):
			n[i-min]=n[i-min]+1
	if(x==max):
		n[max-min-1]=n[max-min-1]+1
	return
#____________________________自定义函数结束__________________________________

piclist=[] #设定图片集
hsvlist=[]

num=3 #设定读取图片数量

i=1
while i<=num: 
    img = cv2.imread('D:/study/python program/zlx/1/'+str(i)+'.jpg')#按排列读取图片集
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #转换bgr2hsv
    
    piclist.append(img) #分别添加正常图片和hsv图片到图片集
    hsvlist.append(hsv)
    i=i+1

pic_arr=np.array(piclist) #将图片集转换成4维张量
hsv_arr=np.array(hsvlist)

m=hsv_arr.shape[1] #导出图片的行列大小
n=hsv_arr.shape[2]

print(m)
print(n)
#__________________________读取图片完毕_________________________________


#利用sobel算子计算图像的梯度:
#cv2.sobel(src,ddepth,dx,dy,[ksize]) ddepth表示图像的深度，
#  当处理为8位图像时，当梯度小于0时，会自动变成0，造成边界图像丢失

sobelist=[] #设定梯度图片集
#一般设置为cv2.CV_64F,先计算hsv的梯度
i=1
while i<=num:
	sobelx=cv2.Sobel(pic_arr[i-1],cv2.CV_64F,dx=1,dy=0) #x方向的,使cv2.convertScaleAbs()函数将结果转化为原来的uint8的形式
	sobelx=cv2.convertScaleAbs(sobelx)
	sobely=cv2.Sobel(pic_arr[i-1],cv2.CV_64F,dx=0,dy=1) #y方向的
	sobely=cv2.convertScaleAbs(sobely)
	result1=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  #综合考虑x方向和y方向的梯度权重
	sobelist.append(result1)
	i=i+1

sobel_arr=np.array(sobelist)#设置梯度张量集
'''
#计算bgr梯度
sobelx=cv2.Sobel(pic_arr[2],cv2.CV_64F,dx=1,dy=0)  	  #x方向的
#使cv2.convertScaleAbs()函数将结果转化为原来的uint8的形式
sobelx=cv2.convertScaleAbs(sobelx)

sobely=cv2.Sobel(pic_arr[2],cv2.CV_64F,dx=0,dy=1) #y方向的
sobely=cv2.convertScaleAbs(sobely)

result2=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  #x方向和y方向的梯度权重
'''
#展示梯度处理之后图像
cv2.namedWindow('result', 0)
cv2.imshow("result",sobel_arr[2])
#_______________________梯度处理结束______________________________
'''
#计算背景平均hsv分布:
H=0
S=0
V=0

for i in range(0,m):
	print(i)
	for j in range(0,n):
		H=H+(sobel_arr[2,i,j,0])
		S=S+(sobel_arr[2,i,j,1])
		V=V+(sobel_arr[2,i,j,2])

print(H/(m*n))
print(S/(m*n))
print(V/(m*n))
'''

#______________________ 计算平均hsv结束____________________________

#进一步筛选梯度图像：
hmin=0#为增加效率，不妨先设定基础值,认为背景出现在这个区域内
hmax=50

smin=0
smax=50

vmin=0
vmax=50

#统计数目
'''
for p in range(0,num): #遍历图像
        hi=np.linspace(0,0,hmax-hmin) #定义计数空间
        hi=np.array(hi)
        si=np.linspace(0,0,smax-smin) #定义计数空间
        si=np.array(si)
        vi=np.linspace(0,0,vmax-vmin) #定义计数空间
        vi=np.array(vi)
        for i in range(0,m): #遍历像素点
                for j in range(0,n):
                        frequent(hmin,hmax,sobel_arr[p,i,j,0],hi)
                        frequent(smin,smax,sobel_arr[p,i,j,1],si)
                        frequent(vmin,vmax,sobel_arr[p,i,j,2],vi)
                print(i)
        print(hi)
        print(si)
        print(vi)
'''
#进一步筛选
copy_arr=sobel_arr

for p in range(0,num): #遍历图像
        for i in range(0,m): #遍历像素点
                for j in range(0,n):
                        if (sobel_arr[p,i,j,0]<=hmax and sobel_arr[p,i,j,0]>=hmin) and (sobel_arr[p,i,j,1]<=smax and sobel_arr[p,i,j,0]>=smin) and (sobel_arr[p,i,j,2]<=vmax and sobel_arr[p,i,j,2]>=vmin):
                                copy_arr[p,i,j]=[0,0,0]
                        #else:
                                #copy_arr[p,i,j]=[0,0,0]
                print(i)


cv2.namedWindow('result0', 0)
cv2.imshow('result0',copy_arr[0])
cv2.namedWindow('result1', 0)
cv2.imshow('result1',copy_arr[1])
cv2.namedWindow('result2', 0)
cv2.imshow('result2',copy_arr[2])
cv2.waitKey(0)