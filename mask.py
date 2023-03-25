import cv2 as cv
import numpy as np

img=cv.imread('Photos/p5.jpeg')

blank=np.zeros(img.shape[:2],dtype='uint8')

circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),50,255,-1)

masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',masked)

cv.waitKey(0)