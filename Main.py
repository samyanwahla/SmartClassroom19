import cv2,glob
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time
from CombineIP import IPfunctions as FD
from bezierclasss import beziercurve as bz

##root = Tk()
##root.withdraw()
##folder_selected = askdirectory()
##print(folder_selected)
##path=str(folder_selected)+'/*'
##print(path)
##FD.makefolders()
###FD.facedetect(path)
##FD.Lipdetect(FD,path)
##FD.Lefteyedetect(FD,path)
##FD.Righteyedetect(FD,path)
#FD.Binarization(path)
#FD.BeizerCurvePoints(path)
bz.init()



