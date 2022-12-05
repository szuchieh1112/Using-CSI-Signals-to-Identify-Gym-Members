import numpy as np  
import scipy.io as sio 
import csv
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.utils import np_utils 
from matplotlib import pyplot as plt
import pandas as pd 
from sklearn.model_selection import train_test_split


def Creat_data(train):
        X_predict , Y_predict=[],[]
        X_predict.append(np.array(train.iloc[0:len(train),0:30]))
        Y_predict.append(np.array(train.loc[0:len(train),"label"]) )

        X_predict =np.array(X_predict).reshape(-1,30)
        Y_predict = np.array(Y_predict).reshape(-1,1)
        return X_predict,Y_predict


if __name__ == "__main__":
    
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    data  = pd.read_csv(r'D:/1/PCA_ALL.csv',engine='python')
    iris_data , iris_label = Creat_data(data)
    iris_label = iris_label.flatten()
    
    with open('DNNAccuracy.txt', 'a') as writer:
     Accuracy = 0
     Neuber1 = 0
     Neuber2 = 0
     Neuber3 = 0
     Neuber4 = 0
     for i in [10,100,300,500,750,1000]:
      for j in [10,100,300,500,750,1000]:
         Accuracyarry = []

         for z in range(10):
             train_data , test_data , train_label , test_label = train_test_split(iris_data,iris_label,test_size=0.2)
             train_label = np_utils.to_categorical(train_label) 
             test_label = np_utils.to_categorical(test_label) 

             model = Sequential()
            
             model.add(Dense(units= i, input_dim=30, kernel_initializer='normal', activation='relu')) 
             model.add(Dense(units= j, kernel_initializer='normal', activation='relu'))
             # Add output layer
             model.add(Dense(units=2, kernel_initializer='normal', activation='softmax'))

             
             model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 
            
             train_history = model.fit(x=train_data, y=train_label, validation_split=0.2, epochs=200 , batch_size=100, verbose=0)  
             
             scores = model.evaluate(test_data, test_label)  
             Accuracyarry.append((scores[1]*100.0))
             del model

         Accur = round(np.sum(Accuracyarry)/len(Accuracyarry), 4)
         stroutscv = "\t2 [Info] Accuracy = {:2.2f}%,[{},{}]".format(Accur,i,j) 
         print (stroutscv)
         print (stroutscv,file = writer)
         if (Accur > Accuracy):
             Neuber1 = i
             Neuber2 = j
             Accuracy = Accur

    stroutscv = "\t2 hidden [Info] Accuracy = {:2.2f}%,[{},{}]".format(Accuracy,Neuber1,Neuber2) 
    #print (stroutscv,file = writer)
    writer.close()
    
    with open('DNNAccuracy.txt', 'a') as writer:
     
     Accuracy = 0
     Neuber1 = 0
     Neuber2 = 0
     Neuber3 = 0
     Neuber4 = 0
     for i in [10,100,300,500,750,1000]:
      for j in [10,100,300,500,750,1000]:
         Accuracyarry = []
         for z in range(10):
             train_data , test_data , train_label , test_label = train_test_split(iris_data,iris_label,test_size=0.2)
             train_label = np_utils.to_categorical(train_label) 
             test_label = np_utils.to_categorical(test_label) 

             model = Sequential()
             
             model.add(Dense(units= i, input_dim=30, kernel_initializer='normal', activation='relu')) 
             model.add(Dense(units= j, kernel_initializer='normal', activation='relu'))
             model.add(Dense(units= k, kernel_initializer='normal', activation='relu'))
             # Add output layer
             model.add(Dense(units=2, kernel_initializer='normal', activation='softmax'))

             
             model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 
             
             train_history = model.fit(x=train_data, y=train_label, validation_split=0.2, epochs=200 , batch_size=100, verbose=0)  
             
             scores = model.evaluate(test_data, test_label)  
             Accuracyarry.append((scores[1]*100.0))
             del model

         Accur = round(np.sum(Accuracyarry)/len(Accuracyarry), 4)
         stroutscv = "\t3 [Info] Accuracy = {:2.2f}%,[{},{},{}]".format(Accur,i,j,k) 
         print (stroutscv)
         print (stroutscv,file = writer)
         if (Accur > Accuracy):
             Neuber1 = i
             Neuber2 = j
             Neuber3 = k
             Accuracy = Accur

     stroutscv = "\t3 hidden [Info] Accuracy = {:2.2f}%,[{},{},{}]".format(Accuracy,Neuber1,Neuber2,Neuber3) 
     #print (stroutscv,file = writer)
     writer.close()
    '''
    with open('DNNAccuracy.txt', 'a') as writer:

    Accuracy = 0
    Neuber1 = 0
    Neuber2 = 0
    Neuber3 = 0
    Neuber4 = 0
    for i in [10,100,300,500,750,1000]:
     for j in [10,100,300,500,750,1000]:
      for k in [10,100,300,500,750,1000]:
       for l in [10,100,300,500,750,1000]:
        Accuracyarry = []

        for z in range(10):
            train_data , test_data , train_label , test_label = train_test_split(iris_data,iris_label,test_size=0.2)
            test_label = np_utils.to_categorical(test_label) 

            model = Sequential()
            model.add(Dense(units= i, input_dim=30, kernel_initializer='normal', activation='relu')) 
            model.add(Dense(units= j, kernel_initializer='normal', activation='relu'))
            model.add(Dense(units= k, kernel_initializer='normal', activation='relu'))
            model.add(Dense(units= l, kernel_initializer='normal', activation='relu'))
            model.add(Dense(units=2, kernel_initializer='normal', activation='softmax'))
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 
            #train_history = model.fit(x=train_data, y=train_label, validation_split=0.2, epochs=200 , batch_size=100, verbose=0)  
            scores = model.evaluate(test_data, test_label)  
            Accuracyarry.append((scores[1]*100.0))
            del model

        Accur = round(np.sum(Accuracyarry)/len(Accuracyarry), 4)
        stroutscv = "\t4 [Info] Accuracy = {:2.2f}%,[{},{},{},{}]".format(Accur,i,j,k,l) 
        print (stroutscv)
        writer.write(stroutscv)

        if (Accur > Accuracy):
            Neuber1 = i
            Neuber2 = j
            Neuber3 = k
            Neuber4 = l
            Accuracy = Accur
    stroutscv = "\t4 hidden [Info] Accuracy = {:2.2f}%,[{},{},{}]".format(Accuracy,Neuber1,Neuber2,Neuber3,Neuber4) 
    writer.write(stroutscv)
    writer.close()
'''
