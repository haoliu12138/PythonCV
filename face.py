from logging import captureWarnings
import cv2 as cv
capture=cv.VideoCapture(0)
#判断摄像头是否打开
if not capture.isOpened():
    print('摄像头未打开')
else:
    print('摄像头正常打开')
    print('摄像头宽度为',capture.get(cv.CAP_PROP_FRAME_WIDTH))
    print('摄像头高度为',capture.get(cv.CAP_PROP_FRAME_HEIGHT))
while True:
    #获取摄像头的图像
    ret,frame=capture.read()
    if not ret:
        print('未正确读取到图像帧')
        break;
    #读取分类器
    haar_cascade=cv.CascadeClassifier('haar_face.xml')
    #识别人脸
    faces_rect=haar_cascade.detectMultiScale(frame,1.1,5)
    #框出人脸范围
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=2)
    #处理读取到的图像 
    cv.imshow('win',frame)
    
    if cv.waitKey(10)==ord('Q'):
        break

cv.waitKey(0)
