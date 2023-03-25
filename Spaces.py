import cv2 as cv

img=cv.imread('Photos/p5.jpeg')
cv.imshow('img',img)
#RGB图片转灰度图片
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#BGR转HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
#BGR转lab
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)
#BGR转RGB(这里需要注意rgb和bgr)
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

cv.waitKey(0)