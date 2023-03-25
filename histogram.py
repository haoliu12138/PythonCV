from turtle import back
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def gray_hist():
    img=cv.imread('Photos/p5.jpeg')
    cv.imshow('img',img)
    #转灰度图
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('gray',gray)
    #创建mask
    blank=np.zeros(img.shape[:2],dtype='uint8')
    circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),50,255,-1)
    mask=cv.bitwise_and(gray,circle)
    cv.imshow('mask',mask)
    #计算灰度直方图
    gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])

    plt.figure()
    plt.title('hist')
    plt.xlabel('gray')
    plt.ylabel('amount')
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()

    cv.waitKey(0)

img=cv.imread('Photos/p5.jpeg')
cv.imshow('img',img)
#创建mask
blank=np.zeros(img.shape[:2],dtype='uint8')
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),50,255,-1)
cv.imshow('img1',img)
plt.figure()
plt.title('hist')
plt.xlabel('gray')
plt.ylabel('amount')
plt.xlim([0,256])
colors=('b','g','r')
masks=cv.split(img)
for i,color in enumerate(colors):
    #分一个通道出来做蒙版
    mask=cv.bitwise_and(masks[i],circle)
    #计算直方图
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=color)

plt.show()
cv.waitKey(0)