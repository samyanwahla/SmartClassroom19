import cv2,glob
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time
from CombineIP import IPfunctions as FD

root = Tk()
root.withdraw()
folder_selected = askdirectory()
print(folder_selected)
path=str(folder_selected)+'/*.tiff'
print(path)

FD.facedetect(path)
FD.Lipdetect(path)
