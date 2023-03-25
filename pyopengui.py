import pyautogui as gui
import cv2 as cv
import os 
picture_name='win.png'
template_name='Photos/start.png'
# 截取屏幕截图到当前桌面
gui.screenshot(picture_name)
#读取屏幕截图
img=cv.imread(os.path.join(os.getcwd(),picture_name),cv.IMREAD_GRAYSCALE)
#开始按钮模板图片
template=cv.imread(template_name,cv.IMREAD_GRAYSCALE)
#获取模板高和宽
h,w=template.shape
#获取模板匹配结果
res=cv.matchTemplate(img,template,cv.TM_CCOEFF)
minval,maxcal,minloc,maxloc=cv.minMaxLoc(res)
topleft=maxloc
bottonright=(topleft[0]+w,topleft[1]+h)
print(topleft)
print(bottonright)
cv.rectangle(img,topleft,bottonright,0,2)
#输出文件查看结果
cv.imwrite('winres.png',img)
#鼠标移动到匹配模板像素中间点(就是开始按钮)
gui.FAILSAFE =False  

gui.click(topleft[0]+(w//2),topleft[1]+(h//2))

