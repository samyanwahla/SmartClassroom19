

import numpy as np
import csv
from numpy import genfromtxt
import re
from io import StringIO
import collections
import sys
sys.version
import math

def sigmoid(x):

	return 1.0/(1.0 + np.exp(-x))

def sigmoid_der(x):
	return x*(1.0 - x)

##def softmax(A):
##    expA = np.exp(A)
##    return expA / expA.sum(axis=1, keepdims=True)


def softmax(x):
        e_x = np.exp(x - np.max(x)) 

        return e_x / e_x.sum() 

##def softmax(A):
##    expA = np.exp(A)
##    return expA /expA.sum()

class NN:


   
    def __init__(self, inputs):
        
        self.inputs = inputs
##        output_labels = 7
        self.l=9
        self.li=9
##        self.l=len(self.inputs)
##        self.li=len(self.inputs[0])
##        bh = np.random.randn(self.l)
##        bo = np.random.randn(output_labels)
        self.wi=np.random.random((self.li, self.l))
        self.wh=np.random.random((self.l, 1))

    def think(self, inp):
        s1=sigmoid(np.dot(inp, self.wi) )
        s2=softmax(np.dot(s1, self.wh))
        return s2

    def train(self, inputs,outputs, it):

        #*******feed forward**********
        for i in range(it):
            l0=inputs
            l1=sigmoid(np.dot(l0, self.wi)  )    #phase1 ah
            l2=softmax(np.dot(l1, self.wh) )    #phase2 a0
            


            
            l2_err=outputs - l2
##            dzo_dwo = l1
##            dcost_wo = np.dot(dzo_dwo.T , l2)
##            dcost_bo = l2
            l2_delta = np.multiply(l2_err, sigmoid_der(l2))

            
            l1_err=np.dot(l2_delta, self.wh.T)
            l1_delta=np.multiply(l1_err, sigmoid_der(l1))

            self.wh+=np.dot(l1.T, l2_delta)
            self.wi+=np.dot(l0.T, l1_delta)

    
    def accuracy(self , input_values , output , error , accuracy):
            
        
        
        real_output = 0
        flag = 0
        
        for elem in inputs:
                if collections.Counter(elem) == collections.Counter(input_values) :
                        flag = 1           
        if flag == 0:
                print("False Input")
                
                error = error+1
        else:
                error1 = 0
                Y = inputs.tolist()
                actual_input = input_values
##                print("Actual Input" , actual_input )
                a = actual_input[0]
                b = actual_input[1]
                c = actual_input[2]
                d = actual_input[3]
                e = actual_input[4]
                f = actual_input[5]
                for subarray in Y:
                        if a in subarray:
##                                print(Y.index(subarray), '-', subarray.index(a) ,'-', subarray.index(b) ,'-', subarray.index(c),'-', subarray.index(d),'-', subarray.index(e) ,'-', subarray.index(f))
                                index = Y.index(subarray)
                                print("actual input index" ,index )
                actual_output = self.think(inputs[index])
                print("ActualOutput" , actual_output)
                        
##                                errorfinding(output , actual_output)
                if actual_output != output:
                        print("Actual output is not equal to predicted output")
                        
                        error = error + 1
                        print(error)
         
        print("again input Write y")
        inputno1 = input("Enter Y or N: ")
        if inputno1=="Y":
                A = str(input("Input 1: "))
                B = str(input("Input 2: "))
                C = str(input("Input 3: "))
                D = str(input("Input 4: "))
                E = str(input("Input 5: "))
                F = str(input("Input 6: "))
                G = str(input("Input 7: "))
                H = str(input("Input 8: "))
                I = str(input("Input 9: "))
##                print("Output data: ")
                X = np.array([A, B, C,D,E,F,G,H,I ])
                X= X.astype(float)
                predicted_output = self.think(X)
                print('Predicted output is' , predicted_output )
                self.accuracy(X , predicted_output,error ,accuracy)
                
        


        accuracy = error/366
        print ("Accuracy score: " ,accuracy)


    
    
     



#**********************************************Training *************************************************************


# Input from file for training
inputs = np.genfromtxt('Book1.csv' , delimiter=',')
inputs = np.array(inputs)
inputs = np.delete(inputs , 9 , axis = 1)
print(inputs)
##print(softmax(inputs))

# Output from file for training
outputs = np.genfromtxt('Book1.csv' , delimiter=',')
outputs  = np.array(outputs)
outputs  = np.delete(outputs , [0,1,2,3,4,5,6,7,8] , axis = 1)
print(outputs )
##print(softmax(outputs))




def main():
        
        n=NN(inputs)                  # training of dataset
        print('before training')
        print(n.think(inputs))
        print('after training')
        n.train(inputs, outputs, 60000)
        print(n.think(inputs))
        accuracy = 0
        error = 0        
        error1 = 0
        
                
        A = str(input("Input 1: "))
        B = str(input("Input 2: "))
        C = str(input("Input 3: "))
        D = str(input("Input 4: "))
        E = str(input("Input 5: "))
        F = str(input("Input 6: "))
        G = str(input("Input 7: "))
        H = str(input("Input 8: "))
        I = str(input("Input 9: "))
        
        X = np.array([A, B, C,D,E,F ,G,H,I])
        X= X.astype(float)
        predicted_output = n.think(X)
        print('Predicted output is' , predicted_output)
        n.accuracy(X , predicted_output , error , accuracy)


if __name__ == "__main__":
        main()



