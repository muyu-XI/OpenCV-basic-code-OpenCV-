import os
import cv2
import numpy as np
def fresh():
    print(cv2.waitKey(0))  # 让窗口暂停,0即为永久等待
    cv2.destroyAllWindows()

# 基本文件地址配置
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_dir = os.path.join(script_dir,"opencv_logo.jpg")
plane_dir = os.path.join(script_dir,"plane.jpg")
bookpage_dir = os.path.join(script_dir,"bookpage.jpg")
poker_dir = os.path.join(script_dir,"poker.jpg")
# 读取版本号,注意加括号（）！！
print(f"Version:{cv2.getVersionString()}")
# 打印图片的形状（高度，宽度，通道数）
logo = cv2.imread(logo_dir)
print(logo.shape)

# 图像的颜色
# 颜色通道顺序：BGR
cv2.imshow("blue",logo[:,:,0])
cv2.imshow("green",logo[:,:,1])
cv2.imshow("red",logo[:,:,2])
# 彩色图片灰度化
gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
fresh()

# 图像裁剪操作
crop = logo[172:222,31:217].copy() #先纵再横
cv2.imshow("crop",crop)
fresh()

# 实现绘图功能
# 创建黑色画布
image = np.zeros([300,300,3],dtype=np.uint8)
# 绘制线段（对象， 起点， 终点， 颜色， 粗细）
cv2.line(image,(111,111),(222,222),(255,0,0),2) #蓝色
# 绘制矩形（~，起点， 对角点， 颜色， 粗细）
cv2.rectangle(image,(150,150),(180,296),(0,255,0),2)#绿色
# 绘制圆形（~，圆心， 半径， 颜色， 粗细）
cv2.circle(image,(250,165),30,(0,0,255),3) #红色
# 绘制字符串（~， 内容， 坐标， 字体格式序号， 缩放系数，
#           颜色， 粗细， 线条类型序号）
cv2.putText(image,"Hello,World",(100,50),0,1,(255,255,255)
,2,16) #白色
cv2.imshow("image",image)
fresh()

# 图形的滤波
plane = cv2.imread(plane_dir)
# 使用高斯滤波器
gauss = cv2.GaussianBlur(plane,(5,5),0)
# 使用中值滤波器，此外还有双边和均值
median = cv2.medianBlur(plane,5)
cv2.imshow("plane",plane)
cv2.imshow("gauss",gauss)
cv2.imshow("median",median)
fresh()

# 图片特征的提取
# 图片先灰度化
# 获取特征点 （对象， 最多的点数， 
#            质量优度水平， 特征点之间的最小距离）
corners = cv2.goodFeaturesToTrack(gray,500,0.1,10)
# 标记出每个点
logo_feature = logo.copy()
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(logo_feature,(int(x),int(y)),3,(255,0,255),-1) #-1为实心
cv2.imshow("corners",logo_feature)
fresh()

# 图片的模板匹配（以匹配扑克牌上的菱形为例）
poker = cv2.imread(poker_dir)
gray_poker = cv2.cvtColor(poker,cv2.COLOR_BGR2GRAY)
# 选取匹配模板
templates = [gray_poker[97:133,387:417],gray_poker[188:227,351:383]]
# 使用标准相关匹配算法——将待检测对象和模板都标准化再来计算匹配度
for temp in templates:
    match = cv2.matchTemplate(gray_poker,temp,cv2.TM_CCOEFF_NORMED)
# 找出匹配系数大于0.9的匹配点
    locations = np.where(match >=0.9)
# 循环遍历每一个匹配点并画出矩形框标记
    h,w = temp.shape[0:2] 
    for p in zip(*locations[::-1]):
        x1,y1 = p[0],p[1]
        x2,y2 = x1+w,y1+h
        cv2.rectangle(poker,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("poker",poker)
fresh()

# 图像的梯度（明暗变化）
# 使用拉普拉斯算子（检测边缘——梯度剧烈变化处）
laplacian= cv2.Laplacian(gray,cv2.CV_64F)
# canny边缘检测（定义边缘为梯度区间）
# 梯度大于200 -> 变化足够强烈，确定是边缘
# 梯度小于100 -> 变化较为平缓，确定非边缘
# 梯度介于二者之间 -> 待定，看其是否与已知的边缘像素相邻
canny = cv2.Canny(gray,100,200)
cv2.imshow("laplacian",laplacian)
cv2.imshow("canny",canny)
fresh()

# 图片的阈值算法(二值化，将连续的灰度范围切割为白+黑)
gray_book = cv2.imread(bookpage_dir,cv2.IMREAD_GRAYSCALE)
# 图片灰度二值化
ret,binary= cv2.threshold(gray_book,10,255,cv2.THRESH_BINARY)
# 图片自适应二值化（划分区块二值化，效果更好）
adaptive = cv2.adaptiveThreshold(gray_book,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,
155,1)
# 大津算法（基于图片灰度聚类分析，自定义阈值）
ret1,otsu =cv2.threshold(gray_book,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("binary",binary)
cv2.imshow("adaptive",adaptive)
cv2.imshow("otsu",otsu)
fresh()

# 图像的形态学算法（腐蚀和膨胀）
# 在腐蚀和膨胀之前需要先将图片二值化
ret,binary = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
kernal = np.ones((5,5),np.uint8)
# 腐蚀和膨胀操作
erosion = cv2.erode(binary,kernal)
dilation =cv2.dilate(binary,kernal)
cv2.imshow("binary",binary)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
fresh()

# opencv调用电脑中的摄像头
# 获取摄像头设备的指针(设备管理器 -> 照相机)
caputre = cv2.VideoCapture(0)
# 摄像头的读取是连续不断的，需要循环读取
ret = 1
while ret:
    ret,frame=caputre.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray,(5,5),0)
    corners = cv2.goodFeaturesToTrack(gauss,5000 ,0.01,10)
    # 标记出每个点
    frame_feature = frame.copy()
    for corner in corners:
        x,y = corner.ravel()
        cv2.circle(frame_feature,(int(x),int(y)),3,(255,0,255),-1) #-1为实心
        cv2.imshow("feature",frame_feature)
        cv2.imshow("gauss",gauss)

    cv2.imshow("video",frame)
    laplacian= cv2.Laplacian(gauss,cv2.CV_64F)
    # canny边缘检测（定义边缘为梯度区间）
    # 梯度大于200 -> 变化足够强烈，确定是边缘
    # 梯度小于100 -> 变化较为平缓，确定非边缘
    # 梯度介于二者之间 -> 待定，看其是否与已知的边缘像素相邻
    canny = cv2.Canny(gray,100,200)
    cv2.imshow("laplacian",laplacian)
    cv2.imshow("canny",canny)
    key = cv2.waitKey(1) # 等待键盘输入1ms
    if key !=-1:         # 按任意键跳出循环
        break
 # 释放指针
caputre.release()