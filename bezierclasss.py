import tkinter as tk
import math
from math import sqrt
from tkinter import Canvas, mainloop, Tk


class beziercurve(tk.Tk):
     def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.canvas = tk.Canvas(width=400, height=400)
        self.canvas.pack(fill="both", expand=True)
        u=0
        p01all=[0,0]
        p11array=[0,0]
        puarray=[0,0]

        p0=[106,199]
        p1=[340,300]
        p2=[500,199]
        self._create_token(p0,"red")
        ##self._create_token(p1,"red")
        self._create_token(p2,"red")
        self._bezier_curve(p0,p1,p2,u)
        self._draw_curve(xvalues,yvalues)
        



     def _create_token(self,coord, color):
        '''Create a token at the given coordinate in the given color'''
        x=coord[0]
        y=coord[1]
        self.canvas.create_oval(x-5, y-5, x+5, y+5, 
                                outline=color, fill=color, tags="token")
     def _bezier_curve(self,p0,p1,p2,u):
        ##equations
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
        while u<=1:
            p01x=(1-u)*p0[0]+u*p1[0]
            p01y=(1-u)*p0[1]+u*p1[1]
            p11x=(1-u)*p1[0]+u*p2[0]
            p11y=p11=(1-u)*p1[1]+u*p2[1]
            pux= (1-u)*p01x+u*p11x
            puy=(1-u)*p01y+u*p11y

            x=((1-u)**2)*p0[0]+p1[0]*2*u*(1-u)+p2[0]*(u**2)
            y=((1-u)**2)*p0[1]+p1[1]*2*u*(1-u)+p2[1]*(u**2)
            xvalues.append(x)
            yvalues.append(y)
            u+=0.1
        i=0
        j=1
        length=len(xvalues)
        while (xvalues):
             if i<=(len(xvalues)-2) and j<len(yvalues):
                 self.canvas.create_line(xvalues[i],yvalues[i],xvalues[j],yvalues[j])
                 i+=1
                 j+=1
                 length=length-1
             else:
                  break

        

            
      
          
      


if __name__ == "__main__":
    app = beziercurve()
    app.mainloop()

        

        

        
        
