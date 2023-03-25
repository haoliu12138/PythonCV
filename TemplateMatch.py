import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#模板匹配,以灰度图读出图片
img=cv.imread(r'C:\Users\hao\Desktop\opencv(Python)\Photos\win.png',cv.IMREAD_UNCHANGED)
mainwin=cv.imread(r'C:\Users\hao\Desktop\opencv(Python)\Photos\win.png',cv.IMREAD_GRAYSCALE)
btn=cv.imread(r'C:\Users\hao\Desktop\opencv(Python)\Photos\start.png',cv.IMREAD_GRAYSCALE)
#btn.shap 灰度 图输出数组 为 图片高，图片宽 这里的-1是将数组转置了
w,h=btn.shape[::-1]
# 定义模板匹配的方法 这些枚举值都是一些数字
methods=['cv.TM_CCOEFF','cv.TM_CCOEFF_NORMED','cv.TM_CCORR','cv.TM_CCORR_NORMED','cv.TM_SQDIFF','cv.TM_SQDIFF_NORMED']
for meth in methods:
    img_t=img.copy()
    # 这里eval应该是吧字符对应的枚举值取了出来
    method=eval(meth)
    print(meth)
    # 使用模板匹配
    res=cv.matchTemplate(mainwin,btn,method)
    print(cv.minMaxLoc(res))
    minval,maxval,minloc,maxloc=cv.minMaxLoc(res)
    # 取得左上角坐标
    if method in [cv.TM_SQDIFF,cv.TM_SQDIFF_NORMED]:
        top_left=minloc
    else:
        top_left=maxloc
    # 计算右下角坐标 用左上角坐标加模板图片的宽和高
    button_right=(top_left[0]+w,top_left[1]+h)
    
    cv.rectangle(img_t,top_left,button_right,(255,0,0),2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_t,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitl3e(meth)
    plt.show()
cv.waitKey(0)
