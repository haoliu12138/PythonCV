import os
import cv2 as cv
import numpy as np

labels=[]
features=[]

def create_train(path):
    #读取文件夹下的文件夹名称，把这个文件夹名字当作标签
    namelist=os.listdir(path)
    #遍历人名文件夹
    for name in namelist:
        print(name)
        label=namelist.index(name)
        #找到人名下的图片
        datalist=os.listdir(os.path.join(path,name))
        for data in datalist:
            #读取图片
            img=cv.imread(os.path.join(path,name,data))
            #转灰度图
            gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
            #读取 级联分类器
            haar_cascade=cv.CascadeClassifier('haar_face.xml')
            # 识别人脸范围
            face_rect=haar_cascade.detectMultiScale(gray,1.1,3)
            #添加数据到数据集(这里只取图片里的第一张脸)
            for (x,y,w,h) in face_rect:
                face_roi=gray[y:y+h,x:x+w]
                break
            features.append(face_roi)
            labels.append(label)

create_train(r'C:\Users\hao\Desktop\man')
#数据转化为numpy数组
features=np.array(features,dtype='object')
labels=np.array(labels)
print('training .......')
#实例化人脸识别
face_recognizer=cv.face.LBPHFaceRecognizer_create()
#开始训练
face_recognizer.train(features,labels)
#保存
face_recognizer.save('face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)
print('training done')


