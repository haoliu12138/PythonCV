import cv2 as cv 
import numpy as np
#原图
img=cv.imread('Photos/p5.jpeg')
cv.imshow('img',img)
#黑色空白图
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)
#灰度图
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray);
#高斯模糊
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
# #轮廓图
canny =cv.Canny(blur,125,175)
cv.imshow('canny',canny)
# #找出图像的所有轮廓(使用从模糊图找的轮廓图当参数)
contours,hierarchines=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')
#使用threshold
# ret,thresh=cv.threshold(gray,200,255,cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)

#找出边缘上的点
# contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contours found')
#把这些轮廓的坐标画到blank上
cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow('Contours draw',blank)

cv.waitKey(0)