from email.headerregistry import MessageIDHeader
import cv2 as cv 
import numpy as np
#原图
img=cv.imread('Photos/p5.jpeg')
cv.imshow('img',img)
#blur
average=cv.blur(img,(7,7));
cv.imshow('average',average)
print(type(img))
#高斯平滑
GassBlur=cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gass',GassBlur)
#中值模糊
media=cv.medianBlur(img,7);
cv.imshow('media',media);    
#双边滤波
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)