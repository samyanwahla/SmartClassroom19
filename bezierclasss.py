import tkinter as tk
import math
from math import sqrt
from tkinter import Canvas, mainloop, Tk
import cv2,glob
from PIL import Image, ImageDraw
from tkinter.filedialog import askdirectory

class beziercurve(tk.Tk):
     def __init__(self, *args, **kwargs):
##        tk.Tk.__init__(self, *args, **kwargs)

##        self.canvas = tk.Canvas(width=400, height=400)
##        self.canvas.pack(fill="both", expand=True)
##        img = cv2.imread('Drawpoint\Lipa\Lips185.jpg')
        
        u=0
        p01all=[0,0]
        p11array=[0,0]
        puarray=[0,0]

        p0=[3, 28]
        p1=[15, 15]
        p2=[77, 32]
        p3=[8, 40]
        self._bezier_curve(p0,p1,p2,p3,u)
        
        
     


     def _bezier_curve(self,p0,p1,p2,p3,u):
        ##equations

        counter=0

        p01=(1-u)*p0+u*p1
        p11=(1-u)*p1+u*p2
        pu = (1-u)*p01+u*p11
        
        p01x=(1-u)*p0[0]+u*p1[0]
        p01y=(1-u)*p0[1]+u*p1[1]
        p01all=[p01x,p01y]

        p11x=(1-u)*p1[0]+u*p2[0]
        p11y=p11=(1-u)*p1[1]+u*p2[1]
        p11array=[p11x,p11y]

        pux= (1-u)*p01x+u*p11x
        puy=(1-u)*p01y+u*p11y
        puarray=[pux,puy]
        xvalues=[]
        yvalues=[]
        x1values=[]
        y1values=[]

        img = cv2.imread('Drawpoint\Lipa\Lips2.jpg')
             
        while u<=1:
             p01x=(1-u)*p0[0]+u*p1[0]
             p01y=(1-u)*p0[1]+u*p1[1]
             p11x=(1-u)*p1[0]+u*p2[0]
             p11y=p11=(1-u)*p1[1]+u*p2[1]
             pux= (1-u)*p01x+u*p11x
             puy=(1-u)*p01y+u*p11y

             x=((1-u)**2)*p0[0]+p1[0]*2*u*(1-u)+p2[0]*(u**2)
             y=((1-u)**2)*p0[1]+p1[1]*2*u*(1-u)+p2[1]*(u**2)
                 ##botton
             x1=((1-u)**2)*p0[0]+p3[0]*2*u*(1-u)+p2[0]*(u**2)
             y1=((1-u)**2)*p0[1]+p3[1]*2*u*(1-u)+p2[1]*(u**2)
             xvalues.append(x)
             yvalues.append(y)
             x1values.append(x1)
             y1values.append(y1)
             u+=0.1
        i=0
        j=1
        length=len(xvalues)
        while (xvalues):
             if i<=(len(xvalues)-2) and j<len(yvalues):
                  image=cv2.line(img,(int(xvalues[i]),int(yvalues[i])),(int(xvalues[j]),int(yvalues[j])),(0, 0, 255),1)
                  image1=cv2.line(image,(int(x1values[i]),int(y1values[i])),(int(x1values[j]),int(y1values[j])),(0, 0, 255),1)
                  i+=1
                  j+=1
                  length=length-1
             else:
                  break
                  
                  
               
        cv2.imshow('new',image1)
        cv2.imwrite('beziereye/Image2.jpg', image1)
        

             

                 
      
          
      


if __name__ == "__main__":
    app = beziercurve()
    

        

        

        
        
