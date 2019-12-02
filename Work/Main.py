import cv2,glob
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time
from CombineIP import IPfunctions as FD
from bezierclassslips import beziercurvelips as bzLip
from bezierclasssrighteye import beziercurverighteye as bzReye
from bezierclassslefteye import beziercurvelefteye as bzLeye

##root = Tk()
##root.withdraw()
##folder_selected = askdirectory()
##print(folder_selected)
##path=str(folder_selected)+'/*'
##print(path)
##FD.makefolders()
####FD.facedetect(path)
##FD.Lipdetect(FD,path)
##FD.Lefteyedetect(FD,path)
##FD.Righteyedetect(FD,path)
##
##
##root = Tk()
##root.withdraw()
##folder_selected = 'C:\\Users\\Dell\\Desktop\\Work\Parent\Cropped\Lips'
##print(folder_selected)
##path1=str(folder_selected)+'/*'
##print(path1)
##FD.BinarizeLips(FD,path1)
##
##root = Tk()
##root.withdraw()
##folder_selected = 'C:\\Users\\Dell\\Desktop\\Work\Parent\Cropped\LeftEye'
##print(folder_selected)
##path2=str(folder_selected)+'/*'
##print(path2)
##FD.BinarizeLeftEye(FD, path2)
##
##root = Tk()
##root.withdraw()
##folder_selected = 'C:\\Users\\Dell\\Desktop\\Work\Parent\Cropped\RightEye'
##print(folder_selected)
##path3=str(folder_selected)+'/*'
##print(path3)
##FD.BinarizeRightEye(FD, path3)
##root = Tk()
##root.withdraw()
##folder_selected = 'C:\\Users\\Dell\\Desktop\\Work\Parent\Binarize\BinarizeRightEye'
##print(folder_selected)
##path4=str(folder_selected)+'/*'
##print(path4)
##FD.BeizerCurvePointsRightEye(FD, path4)
##
##root = Tk()
##root.withdraw()
##folder_selected = 'C:\\Users\\Dell\\Desktop\\Work\Parent\Binarize\BinarizeLeftEye'
##print(folder_selected)
##path5=str(folder_selected)+'/*'
##print(path5)
##FD.BeizerCurvePointsLeftEye(FD, path5)
##
##root = Tk()
##root.withdraw()
##folder_selected = 'C:\\Users\\Dell\\Desktop\\Work\Parent\Binarize\BinarizeLips'
##print(folder_selected)
##path6=str(folder_selected)+'/*'
##print(path5)
##FD.BeizerCurvePointsLips(FD, path6)

##bzLip.init()
##bzReye.init()
##bzLeye.init()

Features = r'C:\Users\Dell\Desktop\Work\Features.csv'
Features1 = r'C:\Users\Dell\Desktop\Work\Features1.csv'
Features2 = r'C:\Users\Dell\Desktop\Work\Features2.csv'
label = r'C:\Users\Dell\Desktop\Work\label1.csv'
FD._merging_csvfiles(Features,Features1,Features2,label)



