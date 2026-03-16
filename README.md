# OpenCV Basic Code / OpenCV 基础代码

[English](#opencv-basic-code) | [中文](#openCV-基础代码)

---

## 📁 Code Files / 代码文件说明

The complete code of this learning project is stored in two files:  
本学习项目的完整代码分别存放在两个文件中：

| File / 文件 | Description / 说明 |
|------------|-------------------|
| `chapter.py` | Main code file, containing complete examples from basic to advanced levels<br>主要代码文件，包含基础到进阶的完整示例 |
| `testall.py` | Comprehensive test file, including real-time camera processing and advanced applications<br>综合测试文件，包含摄像头实时处理和高级应用 |

---

## English Version

### OpenCV Basic Code

Covering core functional modules of OpenCV:

**Basics**: Image read/write, color channel operations, grayscale conversion, cropping and scaling

**Image Processing**: Gaussian/Median filtering, Canny edge detection, Laplacian gradient, threshold binarization (OTSU/adaptive), erosion and dilation

**Feature Extraction**: Corner detection, contour finding and shape recognition (triangle/rectangle/circle classification)

**Image Transformation**: Perspective correction, template matching

**Advanced Applications**: Haar cascade face detection, HSV color filtering (Trackbar dynamic parameter adjustment)

**Video Processing**: Real-time camera capture, integration of multiple algorithms for dynamic detection

**Utility Functions**: Custom multi-image stacking display

---

#### Detailed Contents

##### I. Basic Image Operations
- **Image Reading and Property Viewing**
  - Read images, view version number, obtain image shape (height, width, channels)
  - Image color channel separation and merging (BGR order)
- **Color Space Conversion**
  - Convert color images to grayscale
  - BGR to HSV color space conversion (for color filtering)
- **Image Cropping and Editing**
  - Image cropping using NumPy array slicing

##### II. Image Drawing Functions
- **Canvas Creation**
  - Create black canvas using NumPy
- **Basic Shape Drawing**
  - Draw lines, rectangles, circles
  - Add text (font, size, color control)

##### III. Image Filtering and Enhancement
- **Filtering Algorithms**
  - Gaussian blur
  - Median blur
- **Edge Detection**
  - Laplacian operator
  - Canny edge detection (dual-threshold algorithm)

##### IV. Image Feature Extraction
- **Corner Detection**
  - goodFeaturesToTrack (Shi-Tomasi corner detection algorithm)
  - Feature point visualization and marking
- **Contour Detection and Shape Recognition**
  - Find contours using findContours
  - Calculate contour area and perimeter
  - Polygon approximation (approxPolyDP)
  - Shape classification (triangle, square, rectangle, circle)

##### V. Image Matching and Transformation
- **Template Matching**
  - matchTemplate using standard correlation matching algorithm
  - Set threshold for matching point selection
  - Draw matching rectangles
- **Geometric Transformation**
  - Image scaling (resize)
  - Perspective transformation (getPerspectiveTransform + warpPerspective)

##### VI. Image Binarization and Morphology
- **Thresholding Algorithms**
  - Global binarization (threshold)
  - Adaptive binarization (adaptiveThreshold)
  - OTSU algorithm
- **Morphological Operations**
  - Erosion
  - Dilation

##### VII. Real-time Video Processing
- **Camera Access**
  - VideoCapture for camera reading
  - Loop for reading video frames
- **Real-time Processing Pipeline**
  - Real-time grayscale conversion, Gaussian filtering
  - Real-time corner detection and marking
  - Real-time edge detection (Laplacian + Canny)

##### VIII. Advanced Applications
- **Face Recognition**
  - Haar cascade classifier usage
  - detectMultiScale for face detection
  - Draw face bounding boxes
- **Color Detection and Filtering**
  - HSV color space application
  - Create Trackbars for dynamic HSV threshold adjustment
  - Generate mask with inRange
  - Implement color extraction with bitwise_and

##### IX. Utility Functions
- **Image Display Helper**
  - fresh function (pause + close windows)
- **Multi-image Stacking Display**
  - Custom stackImages function (automated image stitching, supporting different sizes, automatic grayscale to color conversion)

---

## Chinese Version

### OpenCV 基础代码

涵盖OpenCV核心功能模块：

**基础篇**：图像读写、颜色通道操作、灰度转换、裁剪缩放

**图像处理**：高斯/中值滤波、Canny边缘检测、拉普拉斯梯度、阈值二值化（OTSU/自适应）、腐蚀膨胀

**特征提取**：角点检测、轮廓查找与形状识别（三角形/矩形/圆形分类）

**图像变换**：透视矫正、模板匹配

**高级应用**：Haar级联人脸检测、HSV颜色过滤（Trackbar动态调参）

**视频处理**：摄像头实时调用，集成多种算法进行动态检测

**工具函数**：自定义多图拼板显示

---

#### 详细内容

##### 一、基础图像操作
- **图像读写与属性查看**
  - 读取图像、查看版本号、获取图像形状（高度、宽度、通道数）
  - 图像颜色通道分离与合并（BGR顺序）
- **图像色彩空间转换**
  - 彩色图转灰度图
  - BGR转HSV色彩空间（用于颜色过滤）
- **图像裁剪与编辑**
  - 使用NumPy数组切片实现图像裁剪

##### 二、图像绘制功能
- **创建画布**
  - 使用NumPy创建黑色画布
- **基本图形绘制**
  - 线段、矩形、圆形绘制
  - 文字添加（字体、大小、颜色控制）

##### 三、图像滤波与增强
- **滤波算法**
  - 高斯滤波
  - 中值滤波
- **边缘检测**
  - 拉普拉斯算子
  - Canny边缘检测（双阈值算法）

##### 四、图像特征提取
- **角点检测**
  - goodFeaturesToTrack（Shi-Tomasi角点检测算法）
  - 特征点可视化标记
- **轮廓检测与形状识别**
  - findContours查找轮廓
  - 计算轮廓面积、周长
  - 多边形近似（approxPolyDP）
  - 形状分类（三角形、正方形、长方形、圆形）

##### 五、图像匹配与变换
- **模板匹配**
  - matchTemplate使用标准相关匹配算法
  - 设置阈值筛选匹配点
  - 绘制匹配矩形框
- **几何变换**
  - 图像缩放（resize）
  - 透视变换（getPerspectiveTransform + warpPerspective）

##### 六、图像二值化与形态学
- **阈值算法**
  - 全局二值化（threshold）
  - 自适应二值化（adaptiveThreshold）
  - 大津算法（OTSU）
- **形态学操作**
  - 腐蚀（erode）
  - 膨胀（dilate）

##### 七、实时视频处理
- **摄像头调用**
  - VideoCapture读取摄像头
  - 循环读取视频帧
- **实时处理流水线**
  - 实时灰度化、高斯滤波
  - 实时角点检测与标记
  - 实时边缘检测（Laplacian + Canny）

##### 八、高级应用
- **人脸识别**
  - Haar级联分类器使用
  - detectMultiScale人脸检测
  - 绘制人脸边界框
- **颜色检测与过滤**
  - HSV色彩空间应用
  - 创建Trackbar动态调节HSV阈值
  - inRange生成遮罩
  - bitwise_and实现颜色抠图

##### 九、实用工具函数
- **图像显示辅助**
  - fresh函数（暂停+关闭窗口）
- **多图拼板显示**
  - stackImages自定义函数（自动化拼图，支持不同尺寸、灰度图自动转彩色）

---

### 致敬与致谢 | Acknowledgements

本学习代码参考了以下两位老师的开源项目，在此表示崇高敬意：

This learning code references the following open-source projects, and I would like to express my sincere respect to both teachers:

- **[Murtaza Hassan](https://github.com/murtazahassan)** - [Learn-OpenCV-in-3-hours](https://github.com/murtazahassan/Learn-OpenCV-in-3-hours)
- **[孔范鹤 (Kong Fanhe)](https://github.com/kongfanhe)** - [opencv_tutorial](https://github.com/kongfanhe/opencv_tutorial)

感谢两位老师的优质教程，为本学习过程提供了宝贵指导。

Thanks to both teachers for their excellent tutorials, which provided valuable guidance for this learning journey.
