import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score





class DT:
    def __init__(self, traininp ,testinp , trainout, testout ):
        
        self.traininp = traininp
        self.testinp = testinp
        self.trainout = trainout
        self.testout = testout
        
        self.dt = DecisionTreeClassifier()
        


    def train(self):        
        
        self.dt.fit(self.traininp, self.trainout)
    def test(self):        
               
        predictions = self.dt.predict(self.testinp)
        print(confusion_matrix(self.testout,predictions))
        print(classification_report(self.testout,predictions))
        print(accuracy_score(self.testout,predictions))
        





def main():
        
        dataset = pd.read_csv("weather.csv")
        print(dataset.shape)
        print(dataset.head())

        X = dataset.drop('output', axis=1)
        print(X)
        y = dataset['output']
        print(y)
        

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

        
        n=DT( X_train, X_test, y_train, y_test)
        n.train()
        n.test()

        
        
        


if __name__ == "__main__":
        main()






















