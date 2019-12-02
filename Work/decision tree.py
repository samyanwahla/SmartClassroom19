import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import csv
from numpy import asarray
from numpy import savetxt
from collections import defaultdict, Counter
from csv import DictReader
import tkinter as tk
from PIL import ImageTk,Image  


class DT:
    def __init__(self):
        
##        self.traininp = traininp
##        self.testinp = testinp
####        self.trainout = trainout
##        self.testout = testout
        
        self.dt = DecisionTreeClassifier()
        


    def train(self , traininp , trainout):        
        
        self.dt.fit(traininp, trainout)
    def test(self , testinp , testout):                       
        predictions = self.dt.predict(testinp)
        print(predictions)
    
##        with open("testing.csv") as f:
##            reader = csv.reader(f)
##            i = next(reader)
##            print(i)
##
##        print(i[9])
        
        arr = np.array(predictions)
        dict = {'Prediction': arr}
        df = pd.DataFrame(dict)
        df.to_csv('prediction.csv', index=False )
        print(df)

        print(confusion_matrix(testout,predictions))
        print(classification_report(testout,predictions))
        print(accuracy_score(testout,predictions))


# print_result displays % of emotions       
    def print_result(self):
        with open("prediction.csv") as f:
            a1 = [row["Prediction"] for row in DictReader(f)]
            print(a1)

            list_max_count = []
            smile = (a1.count('1')/11)*100
            list_max_count.append(smile)
            print("Smile % " ,smile)
            
            angry = (a1.count('2')/11) *100
            list_max_count.append(angry)
            print("Angry % " , angry)
                
            sad = (a1.count('3')/11) *100
            list_max_count.append(sad)
            print("Sad % " , sad)
                
            confuse = (a1.count('4')/11)*100
            list_max_count.append(confuse)
            print("Confuse % " ,confuse)
                
            disgust = (a1.count('5')/11)*100
            list_max_count.append(disgust)
            print("Disgust % " ,disgust)
                
            neutral = (a1.count('6')/11)*100
            list_max_count.append(neutral)
            print("Neutral % " ,neutral)
                
            surprise = (a1.count('7')/11)*100
            list_max_count.append(surprise)
            print("Surprise % " ,surprise)


# next code is for displaying net emotion which has highest weightage            
            max_value = max(list_max_count)
##            print(max_value)
            max_index = [i for i, j in enumerate(list_max_count) if j == max_value]
##            print(max_index)
            for value in max_index:
                if value == 0 :
                    print("net emotion is Smile " , list_max_count[0])
                if value == 1 :
                    print("net emotion is Angry  " , list_max_count[1])
                if value == 2 :
                    print("net emotion is Sad " , list_max_count[2])
                if value == 3 :
                    print("net emotion is Confuse " , list_max_count[3])
                if value == 4 :
                    print("net emotion is Disgust " , list_max_count[4])
                if value == 5 :
                    print("net emotion is Neutral " , list_max_count[5])
                if value == 6 :
                    print("net emotion is Surprise " , list_max_count[6])

            




def main():
        
        dataset = pd.read_csv("training.csv")   # training file
##        dataset1 = pd.read_csv("testing.csv")     # testing file

# training
        X = dataset.drop('output', axis=1)
        print(X)
        y = dataset['output']
        print(y)
        

        X_train = X
        y_train = y


#testing        
##        X1 = dataset1.drop('output', axis =1)
##        print("X1" ,X1)
##        print(type(X1))        
##
##        
##        X_test = X1
##        y1 = dataset1['output']
##        y_test = y1
#calling
        
##        n=DT( X_train, X_test, y_train, y_test)
        n = DT()
        n.train(X_train , y_train)
##        n.test(X_test, y_test)
##        n.print_result()



        

        
        


if __name__ == "__main__":
    main()
        






















