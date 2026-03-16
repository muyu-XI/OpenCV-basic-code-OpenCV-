import cv2
import numpy as np
import os
def fresh():
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 修复路径拼接：不要在 Resources 前面加斜杠，否则会被视为绝对路径（导致 script 被丢弃）
lena_path = os.path.join(script_dir, "Resources", "lena.png")

#图像缩放
lena =cv2.imread(lena_path)
lenaResize = cv2.resize(lena,(512,512))
cv2.imshow("lena", lenaResize)
fresh()

#画布补充
img= np.zeros((512,512,3),np.uint8)
#上色
img[:]=255,0,0
#cv2.FILLED表示填充
cv2.rectangle(img,(12,12),(500,500),(0,0,225),cv2.FILLED)
cv2.imshow("img",img)
fresh()

#透视变换
card = cv2.imread(os.path.join(script_dir,"Resources","cards.jpg"))
width,height =250,350
#定义特征点 左上、右上、左下、右下
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
#定义目标形状
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
#计算变换矩阵
matrix = cv2.getPerspectiveTransform(pts1,pts2)
#执行变换
cardOutput =cv2.warpPerspective(card,matrix,(width,height))
cv2.imshow("Output",cardOutput)
cv2.imshow("card",card)
fresh()

#图形同框显示 使用numpy,需要同颜色维度，同大小
#水平堆叠
imgHor = np.hstack((lena,img))
#竖直堆叠
imgVer = np.vstack((lena,img))
cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
fresh()
#收藏，自动化万用拼图板
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#使用Haar 特征级联分类器实现人脸识别
#导入预训练好的模型
faceCascade = cv2.CascadeClassifier(os.path.join(script_dir,"Resources/haarcascade_frontalface_default.xml"))
#预处理
lena_gray = cv2.cvtColor(lena,cv2.COLOR_BGR2GRAY)
#执行检测
faces= faceCascade.detectMultiScale(lena_gray,1.1,4)
#绘制矩形框
for (x,y,w,h) in faces:
    cv2.rectangle(lena,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Result",lena)
fresh()

#形状检测与分类
#图像预处理
shape = cv2.imread(os.path.join(script_dir,"Resources/shapes.png"))
shape_gray = cv2.cvtColor(shape,cv2.COLOR_BGR2GRAY)
shape_gauss = cv2.GaussianBlur(shape_gray,(7,7),1)
shape_canny_a = cv2.Canny(shape_gray,100,200)
shape_canny_b = cv2.Canny (shape_gauss,50,50)
#A. 寻找并筛选轮廓
def getContours(img,imgblur):
    counters,hierarchy = cv2.findContours(imgblur,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    img_draw = img.copy()
    for cnt in counters:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            #-1表示画出全部
            cv2.drawContours(img_draw,cnt,-1,(255,0,0))
#B. 形状近似（数边数）
            perimeter = cv2.arcLength(cnt,True)
            approx =cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h=cv2.boundingRect(approx)
#C. 区分形状，包括正方形与长方形
            if objCor ==3: objectType = "Tri"
            elif objCor ==4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: 
                    objectType="Square"
                else:
                    objectType ="Rectangle"
            elif objCor>4:objectType="Circles"
            else:objectType ="None"
#D.可视化输出
            cv2.rectangle(img_draw,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img_draw,objectType,(x+(w//2)-10,y+(h//2)-10),2,1,(0,0,0),2)
    return img_draw
shape_result1=getContours(shape,shape_canny_a)
shape_result2=getContours(shape,shape_canny_b)
shape_stack = stackImages(0.8,([shape,shape_canny_a,shape_canny_b],[shape_gauss,shape_result1,shape_result2]))
cv2.imshow("shapes",shape_stack)
fresh()

#通过滑动条（Trackbars）实现颜色检测与过滤
lambo = cv2.imread(os.path.join(script_dir,"Resources","lambo.png"))
lambo_HSV = cv2.cvtColor(lambo,cv2.COLOR_BGR2HSV)
# 【阶段 0：辅助工具定义】
# 定义一个空函数，因为创建 Trackbar 必须绑定一个回调函数，这里我们不需要额外操作
def empty(a):
    pass
# 【阶段 1：创建 UI 控制面板】
# 创建一个名为 "TrackBars" 的窗口，并添加 6 个滑动条来动态调整 HSV 的上下限
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
# 【阶段 2：实时读取】
    # 持续读取原图
while True:
# 【阶段 3：获取滑块数值并设定阈值】
    # 实时从 UI 界面读取用户拖动的数值，并封装成 NumPy 数组（颜色范围的向量）
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
# 【阶段 4：颜色过滤与抠图】
    # inRange 生成黑白遮罩（符合范围的变白，不符合的变黑）
    # bitwise_and 利用遮罩把原图中的颜色“扣”出来
    mask = cv2.inRange(lambo_HSV,lower,upper)
    lambo_result = cv2.bitwise_and(lambo,lambo,mask = mask)
# 【阶段 5：多图合并与循环显示】
    # 将四张处理过程图组合在一起显示，方便对比调参
    lamboStack = stackImages(0.6,([lambo,lambo_HSV],[mask,lambo_result]))
    cv2.imshow("Stacked Images",lamboStack)
    cv2.waitKey(1) #必须使用waitkey 1 
    #否则0：你的 while 循环会卡死在第一帧。你每拨动一次滑块，必须在键盘上随便按个键，画面才会更新下一帧