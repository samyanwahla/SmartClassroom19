import cv2,glob
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time

class IPfunctions:

    def makefolders():
        os.makedirs('Parent/Cropped')
        os.makedirs('Parent/Binarize')
        os.makedirs('Parent/Cropped/Lips')
        os.makedirs('Parent/Cropped/LeftEye')
        os.makedirs('Parent/Cropped/RightEye')

    def pathname():
        for root,dirs, filelist in os.walk('C:\\Users\\Nimra\\Desktop\\SmartClassroom19\Parent'):
            for name in dirs:
              if name == 'Cropped':
                 return str( os.path.join(root, name))
                  #for root,dirs, filelist in os.walk(os.path.join(root, name)):
                      #for name in dirs:
                          #if name == 'Lips':
                              #fullname=(os.path.join(root, name))
                             
    
    def facedetect(path):
        
        detect = cv2.CascadeClassifier("C:\pythoncheck\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        for bb,timg in enumerate (glob.glob(path)):
            #print(bb,timg)
            img = cv2.imread(timg)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face = detect.detectMultiScale(gray,1.20,5)
            for(x,y,w,h) in face:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                sub_face = img[y:y+h, x:x+w]
            path1= 'C:\pythoncheck\detect\detect{}.jpg'
            cv2.imwrite(path1.format(bb),sub_face)
            
    def Lipdetect(self,path):
        croppedpath= self.pathname()
        for root,dirs, filelist in os.walk(croppedpath):
            for name in dirs:
                if name == 'Lips':
                    fullname=(os.path.join(root, name))
        fullpath = fullname+"\Lips{}.jpg"
                            
        detect3 = cv2.CascadeClassifier("C:\pythoncheck\Lib\site-packages\cv2\data\haarcascade_smile.xml")
        for bb,timg in enumerate (glob.glob(path)):
            print(bb,timg)
            img = cv2.imread(timg)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            mouth = detect3.detectMultiScale(gray,2,6)
            for(x,y,w,h) in mouth:
                print(x,y)
                print(x+w,y+h)
                if((x> 50 and x+w< 220)and(y >64 and y+h<235)):
                    if((x> 50 and x+w< 220)and(y >150 and y+h<235)):
                      width=x+w
                      height=y+h
                      value = x-90
                      x=x-value
                      value1= y-175
                      y=y-value1
                      value3=width-170
                      width=width-value3
                      value4=height-218
                      height=height-value4
                      w=width-x
                      h=height-y
                      cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
                      sub_face1 = img[y:y+h, x:x+w]
            #path1= 'C:\pythoncheck\Lips\Lips{}.jpg'
            cv2.imwrite(fullpath.format(bb),sub_face1)

    def Lefteyedetect(self,path):
        croppedpath= self.pathname()
        for root,dirs, filelist in os.walk(croppedpath):
            for name in dirs:
                if name == 'RightEye':
                    fullname=(os.path.join(root, name))
        fullpath = fullname+"\RightEye{}.jpg"
        detect1 = cv2.CascadeClassifier("C:\pythoncheck\Lib\site-packages\cv2\data\haarcascade_eye.xml")
        for bb,timg in enumerate (glob.glob(path)):
            print(bb,timg)
            img = cv2.imread(timg)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            lefteye = detect1.detectMultiScale(gray,1.20,5)
            #path3 = 'C:\pythoncheck\RightEye\RightEye{}.jpg'
            
            for(x,y,w,h) in lefteye:
                #print(x,y)
                #print(x+w,y+h)
                if((x> 50 and x+w< 220)and(y >64 and y+h<235)):
                    if((x> 50 and x+w< 220)and(y < 150 and y+h<235)):
                        if((x> 50 and x+w<130)and(y<150 and y+h<235)):
                            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                            sub_face = img[y:y+h, x:x+w]
                            cv2.imwrite(fullpath.format(bb),sub_face)
                            break

    def Righteyedetect(self,path):
        croppedpath= self.pathname()
        for root,dirs, filelist in os.walk(croppedpath):
            for name in dirs:
                if name == 'LeftEye':
                    fullname=(os.path.join(root, name))
        fullpath = fullname+"\LeftEye{}.jpg"
                              
        detect4 = cv2.CascadeClassifier("C:\pythoncheck\Lib\site-packages\cv2\data\haarcascade_lefteye_2splits.xml")
         
        for bb,timg in enumerate (glob.glob(path)):
            print(bb,timg)
            img = cv2.imread(timg)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            righteye = detect4.detectMultiScale(gray,1.20,5)
            #path2= 'C:\pythoncheck\LeftEye\LeftEye{}.jpg'
            for(x,y,w,h) in righteye:
                if((x> 50 and x+w< 220)and(y >64 and y+h<235)):
                    if((x> 50 and x+w< 220)and(y < 150 and y+h<235)):
                        if((x>130 and x+w<220)and(y<150 and y+h<235)):
                            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                            subface1=img[y:y+h, x:x+w]
                            cv2.imwrite(fullpath.format(bb),subface1)
                            break
    
    def BeizerCurvePoints(path):
         for bb,timg in enumerate (glob.glob(path)):
             print(bb,timg)
             img = cv2.imread(timg)
             blur = cv2.GaussianBlur(img, (3,3), 0)
             gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

             thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)[1]

             cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
             cnts = cnts[0] if len(cnts) == 2 else cnts[1]
             c = max(cnts, key=cv2.contourArea)

             left = tuple(c[c[:, :, 0].argmin()][0])
             right = tuple(c[c[:, :, 0].argmax()][0])
             top = tuple(c[c[:, :, 1].argmin()][0])
             bottom = tuple(c[c[:, :, 1].argmax()][0])

             
             cv2.circle(img, left, 8, (0, 50, 255), -1)
             cv2.circle(img, right, 8, (0, 255, 255), -1)
             cv2.circle(img, top, 8, (255, 50, 0), -1)
             cv2.circle(img, bottom, 8, (255, 255, 0), -1)
             print('left: {}'.format(left))
             print('right: {}'.format(right))
             print('top: {}'.format(top))
             print('bottom: {}'.format(bottom))
      
             path = 'C://Users//Dell//Desktop//task//DrawpointLips//Lips{}.jpg'
             cv2.imwrite(path.format(bb),img)
      
             cv2.imshow("Detect Multi Images",img)

    def Binarization(path):
        for bb,timg in enumerate (glob.glob(path)):
            print(bb,timg)
            img = cv2.imread(timg)
            im_gray = cv2.imread(timg, cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            thresh = 80
            im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
     
            path = 'C://Users//Dell//Desktop//task//binarize//Lips{}.jpg'
            cv2.imwrite(path.format(bb),im_bw)
      
            cv2.imshow("Detect Multi Images",im_bw)
            cv2.waitKey(500)
            cv2.destroyAllWindows()

        
    
         
         
     

    
