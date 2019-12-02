import tkinter as tk
import math
from math import sqrt
from tkinter import Canvas, mainloop, Tk
import cv2,glob
from PIL import Image, ImageDraw
from tkinter.filedialog import askdirectory
import csv

class beziercurvelips:
     def init():
##        tk.Tk.__init__(self, *args, **kwargs)
##
##        self.canvas = tk.Canvas(width=400, height=400)
##        self.canvas.pack(fill="both", expand=True)
##        img = cv2.imread('Drawpoint\Lipa\Lips185.jpg')
        data=[['lipswidth','lipsheight','lipsangle']]
        path='lips.csv'
        counter=0
        with open(path) as csvfile:
             readCSV = csv.reader(csvfile, delimiter=',')
             for row in readCSV:
                  p0=[]
                  p1=[]
                  p2=[]
                  p3=[]
                 
                  left = row[0]
                  top = row[1]
                  right = row[2]
                  bottom = row[3]
                  img=row[4]
                  comma=','
                  bracket=')'
                  if (left[2]==str(comma) and left[5]==str(bracket)):
                       x3=left[1]
                       print(x3)
                       y3=left[4]
                       p0.append(int(x3))
                       p0.append(int(y3))
                  else:
                      if(left[2]==str(comma) and left[6]==str(bracket)):
                           x3=left[1]
                           print(x3)
                           y3=left[4]+left[5]
                           p0.append(int(x3))
                           p0.append(int(y3))
                      else:
                            if (left[3]==str(comma) and left[6]==str(bracket)):
                                 x3=left[1]+left[2]
                                 print(x3)
                                 y3=left[5]
                                 p0.append(int(x3))
                                 p0.append(int(y3))
                            else:
                                 if (left[3]==str(comma) and left[7]==str(bracket)):
                                      x3=left[1]+left[2]
                                      print(x3)
                                      y3=left[5]+left[6]
                                      p0.append(int(x3))
                                      p0.append(int(y3))
                                 
                                     
                  print("p0:",p0)
                       #############################
                  

                       
                  if (top[2]==str(comma) and top[5]==str(bracket)):
                       x1=top[1]
                       y1=top[4]
                       p1.append(int(x1))
                       p1.append(int(y1))
                  else:    
                  
                       
                       if(top[2]==str(comma) and top[6]==str(bracket)):
                            x1=top[1]
                            y1=top[4]+top[5]
                            p1.append(int(x1))
                            p1.append(int(y1))
                       else:
                            if (top[3]==str(comma) and top[6]==str(bracket)):
                                 x1=top[1]+top[2]
                                 y1=top[5]
                                 p1.append(int(x1))
                                 p1.append(int(y1))
                            else:
                                 if (top[3]==str(comma) and top[7]==str(bracket)):
                                      x1=top[1]+top[2]
                                      y1=top[5]+top[6]
                                      p1.append(int(x1))
                                      p1.append(int(y1))
                       
                  print("p1:",p1)
                 #############
                  if (right[2]==str(comma) and right[5]==str(bracket)):
                       x2=right[1]
                       y2=right[4]
                       p2.append(int(x2))
                       p2.append(int(y2))
                  else:
                       
                       if(right[2]==str(comma) and right[6]==str(bracket)):
                            x2=right[1]
                            y2=right[4]+right[5]
                            p2.append(int(x2))
                            p2.append(int(y2))
                       else:
                            if (right[3]==str(comma) and right[6]==str(bracket)):
                                 x2=right[1]+right[2]
                                 y2=right[5]
                                 p2.append(int(x2))
                                 p2.append(int(y2))
                            else:
                       
                                 if (right[3]==str(comma) and right[7]==str(bracket)):
                                      x2=right[1]+right[2]
                                      y2=right[5]+right[6]
                                      p2.append(int(x2))
                                      p2.append(int(y2))
                       
                  
                       
                  print("p2:",p2)
                  #################
                  if (bottom[2]==str(comma) and bottom[5]==str(bracket)):
                       x4=bottom[1]
                       y4=bottom[4]
                       p3.append(int(x4))
                       p3.append(int(y4))
                  else:
                       if(bottom[2]==str(comma) and bottom[6]==str(bracket)):
                            x4=bottom[1]
                            y4=bottom[4]+bottom[5]
                            p3.append(int(x4))
                            p3.append(int(y4))
                       else:
                            if (bottom[3]==str(comma) and bottom[6]==str(bracket)):
                                 x4=bottom[1]+bottom[2]
                                 y4=bottom[5]
                                 p3.append(int(x4))
                                 p3.append(int(y4))
                            else:
                       
                  
                       
                                 if (bottom[3]==str(comma) and bottom[7]==str(bracket)):
                                      x4=bottom[1]+bottom[2]
                                      y4=bottom[5]+bottom[6]
                                      p3.append(int(x4))
                                      p3.append(int(y4))
                       
                  
                       
                  print("p3:",p3)
                
                  
                  u=0
                  beziercurvelips._bezier_curve(p0,p1,p2,p3,u,img,counter)
                  width=beziercurvelips._distance(p0,p2)
                  print(width)
                  height=beziercurvelips._distance(p1,p3)
                  print(height)
                  angle=beziercurvelips._angle(p0,p1,p2,width,height)
                  dat=[width,height,angle]
                  counter+=1
                  data.append(dat)             
                     

        
        with open('Features2.csv','w',newline='\n') as fp:
             a=csv.writer(fp,delimiter=',')
             for row in data:
                  a.writerow(row)
         
        a=0
        b=0
        c=0
        p01all=[0,0]
        p11array=[0,0]
        puarray=[0,0]      
        


     def _angle(p0,p1,p2,width,height):
          if (p0[0] != p2[0]):
               avalues01=(p0[0]**2)-(p1[0]**2)
              
               bvalues01=(p0[0])-(p1[0])
             
               equalvalues01=p0[1]-p1[1]
             
     ##          avalues01*a+bvalues*b=equalvalues
               avalues12=(p1[0]**2)-(p2[0]**2)
             
               bvalues12=(p1[0])-(p2[0])
           
               equalvalues12=p1[1]-p2[1]
          
               ##subtraction by multiplivation
               avalues011=avalues01*avalues12
           
               bvalues011=bvalues01*avalues12
           
               equalvalues011=equalvalues01*avalues12
            
               ##
               avalues122=avalues12*avalues01
             
               bvalues122=bvalues12*avalues01
             
               equalvalues122=equalvalues12*avalues01
             
               ##
               avalues=avalues011-avalues122
            
               bvalues=bvalues011-bvalues122
           
               equalvalues=equalvalues011-equalvalues122

               a=0
               b=0
               c=0
               if (avalues==0):
                    if bvalues==0:
                         b='infinity'
                    else:
                         b=equalvalues/bvalues
                     
                         a=(equalvalues01-(b*bvalues01))/avalues01     
                       
                         c=p0[1]-a*(p0[0]**2)-b*(p0[0])
                  
               if ( bvalues==0):
                    if avalues==0:
                         a='infinity'
                    else:
                         a=equalvalues/avalues
                      
                         b=(equalvalues01-(a*avalues01))/bvalues01
                 
                         c=p0[1]-a*(p0[0]**2)-b*(p0[0])
                    
                    
               ##
               slope=((2*a)*p0[0])+b
             

               slope1=(p2[1]-p0[1])/(p2[0]-p0[0])


               o=(slope1-slope)/(1+slope1*slope)
               angle=math.atan(o)
               print(angle)
               return angle
          else:
               angle = 0
               return angle
          
          
          
          
          
               
          
               
          
          
          
          
          
          

          
          
          


     def _distance( p0, p2):
        '''calculate distance between 2 points'''
        return sqrt((p0[0] - p2[0])**2 + (p0[1] - p2[1])**2)   

##     def _bezier_curve(self,p0,p1,p2,p3,u):
     def _bezier_curve(p0,p1,p2,p3,u,img,counter):
        ##equations

##        for bb,timg in enumerate (glob.glob(path)):

             xvalues=[]
             yvalues=[]
             x1values=[]
             y1values=[]

             img = cv2.imread(img)
                  
             while u<=1:


                  x=((1-u)**2)*p0[0]+p1[0]*2*u*(1-u)+p2[0]*(u**2)
                  y=((1-u)**2)*p0[1]+p1[1]*2*u*(1-u)+p2[1]*(u**2)
                  
                      ##botton
                  x1=((1-u)**2)*p0[0]+p3[0]*2*u*(1-u)+p2[0]*(u**2)
                  y1=((1-u)**2)*p0[1]+p3[1]*2*u*(1-u)+p2[1]*(u**2)
                  xvalues.append(x)
                  yvalues.append(y)
                  x1values.append(x1)
                  y1values.append(y1)
                  angle=p0
                  u+=0.1
                  
             i=0
             j=1
             length=len(xvalues)
             while (xvalues):
                  if i<=(len(xvalues)-2) and j<len(yvalues):
                       image=cv2.line(img,(round(xvalues[i]),round(yvalues[i])),(round(xvalues[j]),round(yvalues[j])),(0, 0, 255),1)
                       
                       image1=cv2.line(image,(round(x1values[i]),round(y1values[i])),(round(x1values[j]),round(y1values[j])),(0, 0, 255),1)
                                         
                       
                       i+=1
                       j+=1
                       length=length-1
                  else:
                       break


             
                       
       
##             cv2.imshow('new',image1)
##             cv2.imwrite('beziereye/Image33.jpg', image1)
             
             path = 'beziereye/'
             cv2.imwrite("beziereye/"+str(counter)+".jpg",image1)
           
             cv2.imshow("Detect Multi Images",image1)
                  

                 
      
          
      


if __name__ == "__main__":
     app=beziercurvelips
     app.init()
    

        

        

        
        
