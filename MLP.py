
import numpy as np
import csv
from numpy import genfromtxt
import re
from io import StringIO
import collections
import sys
sys.version

def sigmoid(x):
	return 1.0/(1.0 + np.exp(-x))

def sigmoid_der(x):
	return x*(1.0 - x)

#*************************************************MLP*******************************************************
class NN:


    
    def __init__(self, inputs):
        self.inputs = inputs
##        self.l=len(self.inputs)
##        self.li=len(self.inputs[0])
        self.l=3
        self.li=6

        self.wi=np.random.random((self.li, self.l))
        self.wh=np.random.random((self.l, 1))

    def think(self, inp):
        s1=sigmoid(np.dot(inp, self.wi))
        s2=sigmoid(np.dot(s1, self.wh))
        return s2

    def train(self, inputs,outputs, it):
        for i in range(it):
            l0=inputs
            l1=sigmoid(np.dot(l0, self.wi))
            l2=sigmoid(np.dot(l1, self.wh))

            l2_err=outputs - l2
            l2_delta = np.multiply(l2_err, sigmoid_der(l2))

            l1_err=np.dot(l2_delta, self.wh.T)
            l1_delta=np.multiply(l1_err, sigmoid_der(l1))

            self.wh+=np.dot(l1.T, l2_delta)
            self.wi+=np.dot(l0.T, l1_delta)

   
    def accuracy(self , input_values , output):
            
        
        accuracy = 0
        real_output = 0
        flag = 0
        error = 0
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
##                                print("actual input index" ,index )
                actual_output = self.think(inputs[index])
                print("ActualOutput" , actual_output)
                        
                                
                if actual_output != output:
                        error = error + 1

        accuracy = error/366
        print (accuracy)


    
    
     



#**********************************************Training *************************************************************


# Input from file for training
inputs = np.genfromtxt('weather.csv' , delimiter=',')
inputs = np.array(inputs)
inputs = np.delete(inputs , 6 , axis = 1)
print(inputs)

# Output from file for training
outputs = np.genfromtxt('weather.csv' , delimiter=',')
outputs  = np.array(outputs)
outputs  = np.delete(outputs , [0,1,2,3,4,5] , axis = 1)
print(outputs )







# **************************************** main **************************



def main():
        n=NN(inputs)                  # training of dataset
        print('before training')
        print(n.think(inputs))
        print('after training')
        n.train(inputs, outputs, 60000)
        print(n.think(inputs))
        accuracy = 0
        
        inputno = input("Number of Inputs: ")  # input

        
        error1 = 0
        for x in range(4):
                
                A = str(input("Input 1: "))
                B = str(input("Input 2: "))
                C = str(input("Input 3: "))
                D = str(input("Input 4: "))
                E = str(input("Input 5: "))
                F = str(input("Input 6: "))

                X = np.array([A, B, C,D,E,F ])
                X= X.astype(float)
                predicted_output = n.think(X)
                print('Predicted output is' , predicted_output)

        


if __name__ == "__main__":
        main()








































































































































##
##import numpy as np
##import csv
##from numpy import genfromtxt
##import re
##from io import StringIO
##import collections
##
##def sigmoid(x):
##	return 1.0/(1.0 + np.exp(-x))
##
##def sigmoid_der(x):
##	return x*(1.0 - x)
##
##class NN:
##    def __init__(self, inputs):
##        self.inputs = inputs
##
##        self.l=3
##        self.li=6
##
##        self.wi=np.random.random((self.li, self.l))
##        self.wh=np.random.random((self.l, 1))
##
##    def think(self, inp):
##        s1=sigmoid(np.dot(inp, self.wi))
##        s2=sigmoid(np.dot(s1, self.wh))
##        return s2
##
##    def train(self, inputs,outputs, it):
##        for i in range(it):
##            l0=inputs
##            l1=sigmoid(np.dot(l0, self.wi))
##            l2=sigmoid(np.dot(l1, self.wh))
##
##            l2_err=outputs - l2
##            l2_delta = np.multiply(l2_err, sigmoid_der(l2))
##
##            l1_err=np.dot(l2_delta, self.wh.T)
##            l1_delta=np.multiply(l1_err, sigmoid_der(l1))
##
##            self.wh+=np.dot(l1.T, l2_delta)
##            self.wi+=np.dot(l0.T, l1_delta)
##
##
##
##inputs = np.genfromtxt('weather.csv' , delimiter=',')
##inputs = np.array(inputs)
##inputs = np.delete(inputs , 6 , axis = 1)
##print(inputs)
##
##
##outputs = np.genfromtxt('weather.csv' , delimiter=',')
##outputs  = np.array(outputs)
##outputs  = np.delete(outputs , [0,1,2,3,4,5] , axis = 1)
##print(outputs )
##
##
##
##
##n=NN(inputs)
##print('before training')
##print(n.think(inputs))
##print('after training')
##n.train(inputs, outputs, 60000)
##print(n.think(inputs))
##
##
### *****************Testing**************************************************
##
##
##
##
##A = str(input("Input 1: "))
##B = str(input("Input 2: "))
##C = str(input("Input 3: "))
##D = str(input("Input 4: "))
##E = str(input("Input 5: "))
##F = str(input("Input 6: "))
##
##print("Output data: ")
##X = np.array([A, B, C,D,E,F ])
##X= X.astype(float)
##predicted = n.think(X)
##print('Predicted value is' , predicted)
##
##
##
##
##        
##        
##
##
##
##
##
