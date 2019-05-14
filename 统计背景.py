import cv2
import numpy as np


#需要修改的参数：图片位置及名称，图片数量，筛选背景的初始设定值

#把区域为[min, max]的分布，按间隔为1划成max-min份, 并分配从外部输入数据在此区间的分布,并将结果输出到n数组中
def frequent(min,max,x,n):
	#n=np.linspace(0, 0, max-min)
	for i in range(min, max):
		if (x>=i and x<i+1):
			n[i-min]=n[i-min]+1
	if(x==max):
		n[max-min-1]=n[max-min-1]+1
	return

piclist=[] #设定图片集
hsvlist=[]

num=2 #设定读取图片数量

i=2
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


#将筛选背景的颜色成分等分为很多份，从而寻找出现频率最高的那个，从而定义背景：

hmin=135 #为增加效率，不妨先设定基础值,认为背景出现在这个区域内
hmax=145

smin=120
smax=180

vmin=240
vmax=255

for p in range(0,num): #遍历图像
        hi=np.linspace(0,0,hmax-hmin) #定义计数空间
        hi=np.array(hi)
        si=np.linspace(0,0,smax-smin) #定义计数空间
        si=np.array(si)
        vi=np.linspace(0,0,vmax-vmin) #定义计数空间
        vi=np.array(vi)
        for i in range(0,m): #遍历像素点
                for j in range(0,n):
                        frequent(hmin,hmax,hsv_arr[p,i,j,0],hi)
                        frequent(smin,smax,hsv_arr[p,i,j,1],si)
                        frequent(vmin,vmax,hsv_arr[p,i,j,2],vi)
                print(i)
        print(hi)
        print(si)
        print(vi)