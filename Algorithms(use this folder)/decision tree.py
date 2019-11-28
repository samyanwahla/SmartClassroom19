import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score





class DT:
    def __init__(self, traininp ,testinp , trainout ,testout):
        
        self.traininp = traininp
        self.testinp = testinp
        self.trainout = trainout
        self.testout = testout
        
        self.dt = DecisionTreeClassifier()
        


    def train(self):        
        
        self.dt.fit(self.traininp, self.trainout)
    def test(self):        
               
        predictions = self.dt.predict(self.testinp)
        print(predictions)
        print(confusion_matrix(self.testinp,predictions))
        print(classification_report(self.testinp,predictions))
        print(accuracy_score(self.testinp,predictions))
        





def main():
        
        dataset = pd.read_csv("weather.csv")
        dataset1 = pd.read_csv("Book1.csv")
        print(dataset.shape)
        print(dataset.head())

        X = dataset.drop('output', axis=1)
        print(X)
        y = dataset['output']
        print(y)

        X_train = X
        y_train = y
##
        X1 = dataset1.drop('output', axis=1)
        print(X1)
        X_test = X1

        y1 = dataset1['output']
        y_test = y1
        

##        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        print(X_train.shape)
        print(X_test.shape)
        print(y_train.shape)
        print(y_test.shape)

##        
##        print(y_test.shape)
        

        
        n=DT( X_train, X_test, y_train, y_test)
        n.train()
        n.test()

        
        
        


if __name__ == "__main__":
        main()






















