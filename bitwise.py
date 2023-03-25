import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)
# bitwise and 
bitwiseand=cv.bitwise_and(rectangle,circle)
cv.imshow('bitwiseand',bitwiseand)
#bitwise or
bitwiseor=cv.bitwise_or(rectangle,circle)
cv.imshow('bitwiseor',bitwiseor)
#bitwise xor
bitwisexor=cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwisexor',bitwisexor)
#bitwise not
bitwisenot=cv.bitwise_not(rectangle)
cv.imshow('bitwisenot',bitwisenot)

cv.waitKey(0)

