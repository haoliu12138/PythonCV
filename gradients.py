import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/p5.jpeg')
cv.imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#拉普拉斯梯度
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Lap',lap)
#索贝尔梯度
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combine_sobel=cv.bitwise_or(sobelx,sobely)

cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('combine_sobel',combine_sobel)

canny=cv.Canny(gray,150,175)
cv.imshow('canny',canny)



cv.waitKey(0)