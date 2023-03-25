import cv2 as cv
import numpy as np

img=cv.imread('Photos/blue.png')
cv.imshow('img',img)
#blank
blank=np.zeros(img.shape[:2],dtype='uint8')
#分开rgb通道
b,g,r=cv.split(img)

cv.imshow('r',r)
cv.imshow('g',g)
cv.imshow('b',b)

#合并通道
merge=cv.merge([b,g,r])
cv.imshow('merge',merge)

blue=cv.merge([b,blank,blank])
cv.imshow('blue',blue)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

cv.waitKey(0)