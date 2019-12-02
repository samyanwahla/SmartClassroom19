import cv2,glob
from tkinter import *
from tkinter.filedialog import askdirectory
import os
import time
import csv

class IPfunctions:

    def makefolders():
        os.makedirs('Parent/Cropped')
        os.makedirs('Parent/Binarize')
        os.makedirs('Parent/Binarize/BinarizeLips')
        os.makedirs('Parent/Binarize/BinarizeLeftEye')
        os.makedirs('Parent/Binarize/BinarizeRightEye')
        os.makedirs('Parent/Cropped/Lips')
        os.makedirs('Parent/Cropped/LeftEye')
        os.makedirs('Parent/Cropped/RightEye')
        os.makedirs('Parent/Beizar')
        os.makedirs('Parent/Beizar/BeizarLips')
        os.makedirs('Parent/Beizar/BeizarLeftEye')
        os.makedirs('Parent/Beizar/BeizarRightEye')
        
       

    def pathname():
        for root,dirs, filelist in os.walk('C:\\Users\\Dell\\Desktop\\Work\Parent'):
            for name in dirs:
              if name == 'Cropped':
                 return str( os.path.join(root, name))
##              elif name == 'Binarize':
##                  return str(os.path.join(root, name))
##              else:
##                    print('error')
    def pathname1():
        
        for root,dirs, filelist in os.walk('C:\\Users\\Dell\\Desktop\\Work\Parent'):
            for name in dirs:
              if name == 'Binarize':
                 return str(os.path.join(root, name))
                             

    def pathname2():
        
        for root,dirs, filelist in os.walk('C:\\Users\\Dell\\Desktop\\Work\Parent'):
            for name in dirs:
              if name == 'Beizar':
                 return str(os.path.join(root, name))
                
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
                            
        detect3 = cv2.CascadeClassifier("C:\Program Files\Python36\Lib\site-packages\cv2\data\haarcascade_smile.xml")
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
        detect1 = cv2.CascadeClassifier("C:\Program Files\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml")
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
                              
        detect4 = cv2.CascadeClassifier("C:\Program Files\Python36\Lib\site-packages\cv2\data\haarcascade_lefteye_2splits.xml")
         
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

#It will binarize Lips
    def BinarizeLips(self, path):
        binarizeLips = self.pathname1()
        for root, dirs, filelist in os.walk(binarizeLips):
            for dirname in dirs:
                if dirname == 'BinarizeLips':
                    fullname = (os.path.join(root, dirname))
        fullpath = fullname+"\BinarizeLips{}.jpg"
        print(fullpath)
        for bb,timg in enumerate (glob.glob(path)):
            print(bb,timg)
            img = cv2.imread(timg)
            im_gray = cv2.imread(timg, cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            thresh = 80
            im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
            cv2.imwrite(fullpath.format(bb),im_bw)
      
            cv2.imshow("Detect Multi Images",im_bw)
            cv2.waitKey(500)
            cv2.destroyAllWindows()

#It will binarize Left Eye
    def BinarizeLeftEye(self, path):
        binarizeLips = self.pathname1()
        for root, dirs, filelist in os.walk(binarizeLips):
            for dirname in dirs:
                if dirname == 'BinarizeLeftEye':
                    fullname = (os.path.join(root, dirname))
        fullpath = fullname+"\BinarizeLeftEye{}.jpg"
        print(fullpath)
                    
        for bb,timg in enumerate (glob.glob(path)):
            print(bb,timg)
            img = cv2.imread(timg)
            im_gray = cv2.imread(timg, cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            thresh = 80
            im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
            cv2.imwrite(fullpath.format(bb),im_bw)
      
            cv2.imshow("Detect Multi Images",im_bw)
            cv2.waitKey(500)
            cv2.destroyAllWindows()



#It will binarize Right Eye
    def BinarizeRightEye(self, path):
        binarizeLips = self.pathname1()
        for root, dirs, filelist in os.walk(binarizeLips):
            for dirname in dirs:
                if dirname == 'BinarizeRightEye':
                    fullname = (os.path.join(root, dirname))
        fullpath = fullname+"\BinarizeRightEye{}.jpg"
        print(fullpath)
                    
        for bb,timg in enumerate (glob.glob(path)):
            print(bb,timg)
            img = cv2.imread(timg)
            im_gray = cv2.imread(timg, cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            thresh = 80
            im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
            cv2.imwrite(fullpath.format(bb),im_bw)
      
            cv2.imshow("Detect Multi Images",im_bw)
            cv2.waitKey(500)
            cv2.destroyAllWindows()

#It will Draw Byzer points of Lips
 
    def BeizerCurvePointsRightEye(self, path):
        beizarRightEye = self.pathname2()
        for root, dirs, filelist in os.walk(beizarRightEye):
            for dirname in dirs:
                if dirname == 'BeizarRightEye':
                    fullname = (os.path.join(root, dirname))
        fullpath = fullname+"\BeizarRightEye{}.jpg"
        print(fullpath)
        
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

             
            cv2.circle(img, left, 4, (0, 50, 255), -1)
            cv2.circle(img, right, 4, (0, 255, 255), -1)
            cv2.circle(img, top, 4, (255, 50, 0), -1)
            cv2.circle(img, bottom, 4, (255, 255, 0), -1)
            print('left: {}'.format(left))
            print('right: {}'.format(right))
            print('top: {}'.format(top))
            print('bottom: {}'.format(bottom))
            array = [left, right, top, bottom]
            print(array)
            with open('righteye.csv', 'a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([left, right, top, bottom, timg])
                cv2.imwrite(fullpath.format(bb),img)
                cv2.imshow("Detect Multi Images",img)


#It will Draw Byzer points of Left Eye
 
    def BeizerCurvePointsLeftEye(self, path):
        beizarLeftEye = self.pathname2()
        for root, dirs, filelist in os.walk(beizarLeftEye):
            for dirname in dirs:
                if dirname == 'BeizarLeftEye':
                    fullname = (os.path.join(root, dirname))
        fullpath = fullname+"\BeizarLeftEye{}.jpg"
        print(fullpath)
        
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

             
            cv2.circle(img, left, 4, (0, 50, 255), -1)
            cv2.circle(img, right, 4, (0, 255, 255), -1)
            cv2.circle(img, top, 4, (255, 50, 0), -1)
            cv2.circle(img, bottom, 4, (255, 255, 0), -1)
            print('left: {}'.format(left))
            print('right: {}'.format(right))
            print('top: {}'.format(top))
            print('bottom: {}'.format(bottom))
            array = [left, right, top, bottom]
            print(array)
            with open('lifteye.csv', 'a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([left, right, top, bottom, timg])
                cv2.imwrite(fullpath.format(bb),img)
                cv2.imshow("Detect Multi Images",img)

            

#It will Draw Byzer points of Lips
 
    def BeizerCurvePointsLips(self, path):
        beizarLips= self.pathname2()
        for root, dirs, filelist in os.walk(beizarLips):
            for dirname in dirs:
                if dirname == 'BeizarLips':
                    fullname = (os.path.join(root, dirname))
        fullpath = fullname+"\BeizarLips{}.jpg"
        print(fullpath)
        
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
            cv2.circle(img, left, 4, (0, 50, 255), -1)
            cv2.circle(img, right, 4, (0, 255, 255), -1)
            cv2.circle(img, top, 4, (255, 50, 0), -1)
            cv2.circle(img, bottom, 4, (255, 255, 0), -1)
            print('left: {}'.format(left))
            print('right: {}'.format(right))
            print('top: {}'.format(top))
            print('bottom: {}'.format(bottom))
            array = [left, right, top, bottom]
            print(array)
            with open('lips.csv', 'a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([left, right, top, bottom, timg])
                cv2.imwrite(fullpath.format(bb),img)
                cv2.imshow("Detect Multi Images",img)


    def _merging_csvfiles(Features,Features1,Features2,label):
         files=['Features','Features1','Features2','label']
         line_count = 0
         column=[]
         i=0
         column2=[]
         column3=[]
         label = []
         for file in files:
             with open('Features1.csv','r') as f1:
                 csv_reader = csv.reader(f1,delimiter=',')
                 for row1 in csv_reader:
                     column.append(row1)
             with open('Features2.csv','r') as f2:
                 csv_reader2 = csv.reader(f2,delimiter=',')
                 for row2 in csv_reader2:
                     column2.append(row2)
             with open('Features.csv','r') as f3:
                 csv_reader3 = csv.reader(f3,delimiter=',')
                 for row3 in csv_reader3:
                     column3.append(row3)
             with open('label1.csv','r') as f4:
                 csv_reader4 = csv.reader(f4,delimiter=',')
                 for row4 in csv_reader4:
                     label.append(row4)

             with open('Traindata.csv','a',newline='') as f2:
                 csv_writer = csv.writer(f2, delimiter=',')
                 while(column):
                     data=column[i] + column2[i] + column3[i] + label[i]
                     i+=1
                     csv_writer.writerow(data)


          
          
    

                
                
            
    
         
         
     

    
