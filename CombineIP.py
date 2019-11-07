import cv2,glob
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time

class IPfunctions:
    
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
            
    def Lipdetect(path):
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
            path1= 'C:\pythoncheck\Lips\Lips{}.jpg'
            cv2.imwrite(path1.format(bb),sub_face1)
        

    
