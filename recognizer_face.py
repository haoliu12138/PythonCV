import cv2 as cv
import numpy as np
names=['yunlong','shantianxiaozhi','xiaolixun']
img=cv.imread(r'C:\Users\hao\Desktop\20220905134236.jpg');
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 载入人脸范围
haar_cascade=cv.CascadeClassifier('haar_face.xml')
# 识别人脸范围
face_rect=haar_cascade.detectMultiScale(gray,1.1,3)

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

for (x,y,w,h) in face_rect:
    #获取面部矩阵
    face_roi=gray[y:y+h,x:x+w]
    #把矩阵扔进去预测
    label,confidence=face_recognizer.predict(face_roi)
    print(f'{names[label]} confident {confidence}')
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=2)
    cv.putText(img,str(names[label]),(40,40),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),thickness=2)
    break
cv.imshow('predit',img)
cv.waitKey(0)
