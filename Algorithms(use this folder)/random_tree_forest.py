import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score



class RTF:
    def __init__(self, traininp ,testinp , trainout, testout ):
        
        self.traininp = traininp
        self.testinp = testinp
        self.trainout = trainout
        self.testout = testout
        
        self.rtf = RandomForestClassifier(n_estimators = 16, criterion = 'entropy', random_state = 42)
        self.scaler = StandardScaler()


    def train(self):        
        self.scaler.fit(self.traininp)
        self.traininp = self.scaler.transform(self.traininp)
        
        self.rtf.fit(self.traininp, self.trainout)
    def test(self):        
        
        self.testinp = self.scaler.transform(self.testinp)
        predictions = self.rtf.predict(self.testinp)
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
        

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 21)
        
        n=RTF( X_train, X_test, y_train, y_test)
        n.train()
        n.test()

        
        
        


if __name__ == "__main__":
        main()


    


##dataset = pd.read_csv("weather.csv")
##print(dataset.shape)
##print(dataset.head())
##
##X = dataset.drop('output', axis=1)
##print(X)
##y = dataset['output']
##print(y)
##
##X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 21)
##
##scaler = StandardScaler()
##X_train = scaler.fit_transform(X_train)
##X_test = scaler.transform(X_test)
##
##
##classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 42)
##classifier.fit(X_train, y_train)
##
##
##y_pred = classifier.predict(X_test)
##
##print(confusion_matrix(y_test,y_pred))
##print(classification_report(y_test,y_pred))
##print(accuracy_score(y_test, y_pred))
##
