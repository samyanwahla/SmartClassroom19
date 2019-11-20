from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler


class NN:

    def __init__(self, traininp ,testinp , trainout, testout ):
        
        self.traininp = traininp
        self.testinp = testinp
        self.trainout = trainout
        self.testout = testout
##        self.Xtrain = traininp
##        self.Xtest = testinp
##        self.ytrain = trainout
##        self.ytest = testout
        self.mlp = MLPClassifier(hidden_layer_sizes=(9, 5, 7), max_iter=1000)
        self.scaler = StandardScaler()

    def train(self):
        
##        print(self.traininp.shape)
##        print(self.testinp.shape)
        
        self.scaler.fit(self.traininp)
        self.traininp = self.scaler.transform(self.traininp)

        self.mlp.fit(self.traininp, self.trainout)

        
##        self.mlp.fit(self.traininp, self.trainout.ravel())
        

    def test(self):

        self.testinp = self.scaler.transform(self.testinp)
        predictions = self.mlp.predict(self.testinp)
        print(confusion_matrix(self.testout,predictions))
        print(confusion_matrix(self.testout,predictions))
        print(classification_report(self.testout,predictions))
        



def main():
        
##        df = pd.read_csv('weather.csv') 
##        print(df.shape)
##        df.describe().transpose()
##
##
##        target_column = ['output']
##        print(target_column)
##        predictors = list(set(list(df.columns))-set(target_column))
##        df[predictors] = df[predictors]/df[predictors].max()
##
##        X = df[predictors].values
##        y = df[target_column].values
##        print(X)
##        print(y)

        dataset = pd.read_csv("weather.csv")
        print(dataset.shape)
        print(dataset.head())

        X = dataset.drop('output', axis=1)
        print(X)
        y = dataset['output']
        print(y)
        

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        
        n=NN( X_train, X_test, y_train, y_test)
        n.train()
        n.test()

        
        
        


if __name__ == "__main__":
        main()
