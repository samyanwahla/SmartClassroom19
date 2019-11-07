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
    
