import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/p5.jpeg')
cv.imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#简单阈值
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh_inv',thresh)

#自适应阈值
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,9)
cv.imshow('adapt',adaptive_thresh)

cv.waitKey(0)