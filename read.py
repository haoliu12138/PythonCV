import cv2 as cv
#读取图片
def readImg(path):
    img=cv.imread(path)
    
    print('图片高度',img.shape[0])
    print('图片宽度',img.shape[1])

    reimage=cv.resize(img,(1200,675))
    cv.imshow('img',reimage)

    print('重置图片高度',reimage.shape[0])
    print('重置图片宽度',reimage.shape[1])
    cv.waitKey(5000)
capture=cv.VideoCapture(0)
#读取摄像头
def readCam():
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
        #处理读取到的图像 
        #这里吧RGB图像转化为了灰度图像
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('Cam',gray)
        #不设置waitKey的化会卡住，设置为0的化,waitKey的返回值为对应按键的ascall码
        #这里其实就是执行了一个循环，用waitKey来设置中间的间隔时间
        if cv.waitKey(20)==ord('q'):
            break
    #关闭相机
    capture.release()
    cv.destroyAllWindows()
readImg('Photos/743921d05861e813f41c0153a2b3e597.jpeg')