#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np      
import pandas as pd
import matplotlib.pyplot as plt
import sklearn


# In[11]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[22]:




for i in range(0,4):
    print('1.INDIA')
    print('2.AUSTRALIA')
    print('3.ENGLAND')
    print('4.Exit')
    x=int(input('ENTER THE CHOICE'))
    if x==1:
        for i in range(0,3):
            print('1.T20')
            print('2.ODI')
            print('3.TEST')
            print('4.EXIT')
            y=int(input('ENTER THE FORMAT'))
            if y==1:
                print('T20')
                import numpy as np      
                import pandas as pd
                import matplotlib.pyplot as plt
                
                #importing dataset
                dataset=pd.read_csv('india_t20.csv')
                print('*******PLAYING  11 PREDICTOR*********')            
                print('=========')
                print('INDIA T20')
                print('=========')
                c=int(input('1.ENTER THE NUMBER OF BATSMAN'))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS'))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS'))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('enter your choice'))
                            if a==1:
                        
                                print('=======')
                                print('BATSMAN')
                                print('=======')
                                X=dataset.iloc[:,[4,5,7]].values      
                                Y=dataset.iloc[:,[9]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                from sklearn.linear_model import LinearRegression
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_t20_test.csv')
                                X1=dataset1.iloc[:,[4,5,7]].values      
                                Y1=dataset1.iloc[:,[9]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("result1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('result1.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                
                                print('======')
                                print('BOWLER')
                                print('======')
                                                
                                X=dataset.iloc[:,[4,13]].values      
                                Y=dataset.iloc[:,[15]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                from sklearn.linear_model import LinearRegression
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_t20_test.csv')
                                X1=dataset1.iloc[:,[4,13]].values      
                                Y1=dataset1.iloc[:,[15]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("result2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('result2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print('BOWLERS')
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('============')
                                print('WICKETKEEPER')
                                print('============')
                                X=dataset.iloc[:,[13,17]].values      
                                Y=dataset.iloc[:,[18]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                from sklearn.linear_model import LinearRegression
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_t20_test.csv')
                                X1=dataset1.iloc[:,[13,17]].values      
                                Y1=dataset1.iloc[:,[18]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("result3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('result3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(e))
                                
                else:
                        print('THE SUM OF ALL PLAYERS SHOULD BE 11')
                        
            elif y==2:
                print('ODI')
                
                
                #importing dataset
                dataset=pd.read_csv('india_odi.csv')
                print('*******PLAYING  11 PREDICTOR*********')
                print('=========')
                print('INDIA ODI')
                print('=========')
                c=int(input('1.ENTER THE NUMBER OF BATSMAN'))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS'))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS'))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('enter your choice'))
                            if a==1:
                                print('=======')
                                print('BATSMAN')
                                print('=======')
                                X=dataset.iloc[:,[4,5,7]].values      
                                Y=dataset.iloc[:,[9]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_odi_test.csv')
                                X1=dataset1.iloc[:,[4,5,7]].values      
                                Y1=dataset1.iloc[:,[9]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("result1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('result1.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('======')
                                print('BOWLER')
                                print('======')
                                X=dataset.iloc[:,[10,11,12]].values      
                                Y=dataset.iloc[:,[15]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_odi_test.csv')
                                X1=dataset1.iloc[:,[10,11,12]].values      
                                Y1=dataset1.iloc[:,[15]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("result2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('result2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print('BOWLERS')
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('=============')
                                print('WICKET KEEPER')
                                print('=============')
                                
                                
                                X=dataset.iloc[:,[13,16]].values      
                                Y=dataset.iloc[:,[17]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_odi_test.csv')
                                X1=dataset1.iloc[:,[13,16]].values      
                                Y1=dataset1.iloc[:,[17]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("result3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('result3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(e))
                                
                else:
                        print('THE SUM OF ALL PLAYERS SHOULD BE 11')
        
            elif y==3:
                print('TEST')
                
                
                dataset=pd.read_csv('india_test.csv')
                
                print('*******PLAYING  11 PREDICTOR*********')
                print('================')
                print('INDIA TEST MATCH')
                print('================')
                c=int(input('1.ENTER THE NUMBER OF BATSMAN'))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS'))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS'))
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('enter your choice'))
                            if a==1:
                                print('=======')
                                print('BATSMAN')
                                print('=======')                
                                X=dataset.iloc[:,[4,5,6]].values      
                                Y=dataset.iloc[:,[7]].values
                                #splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                              
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_test_test.csv')
                                X1=dataset1.iloc[:,[4,5,6]].values      
                                Y1=dataset1.iloc[:,[7]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("resultindtest1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('resultindtest1.csv')
                                X3=dataset2.iloc[:,:].values
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('======')
                                print('BOWLER')
                                print('======')                
                                X=dataset.iloc[:,[4,5,7]].values      
                                Y=dataset.iloc[:,[9]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_test_test.csv')
                                X1=dataset1.iloc[:,[4,5,7]].values      
                                Y1=dataset1.iloc[:,[9]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("resultindtest2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('resultindtest2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print('BOWLERS')
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('===========')
                                print('wicketkeper')
                                print('===========')                
                                X=dataset.iloc[:,[9,13]].values      
                                Y=dataset.iloc[:,[14]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('india_test_test.csv')
                                X1=dataset1.iloc[:,[9,13]].values      
                                Y1=dataset1.iloc[:,[14]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("resultindtest3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('resultindtest3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(e))
                

            elif y==4:
                break
                        
    elif x==2:
        for i in range(0,3):
            print('1.T20')
            print('2.ODI')
            print('3.TEST')
            print('4.EXIT')
            y=int(input('ENTER THE FORMAT'))
            if y==1:
                               

                print('=====================T20=====================')
                
                
                
                c=int(input('1.ENTER THE NUMBER OF BATSMAN'))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS'))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS'))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('enter your choice'))
                            if a==1:
                        
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('aust201.csv')
                                
                                X=dataset.iloc[:,[3,4,5,6]].values      
                                Y=dataset.iloc[:,[8]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,4,5,6]].values      
                                Y1=dataset1.iloc[:,[8]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("resultfff.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('resultfff.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('BOWLER')
                        
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('aust201.csv')
                                
                                X=dataset.iloc[:,[3,9,10]].values      
                                Y=dataset.iloc[:,[12]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,9,10]].values      
                                Y1=dataset1.iloc[:,[12]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("resultff.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('resultff.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print('BOWLERS')
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('WICKETKEPPER')
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('aust201.csv')
                                
                                X=dataset.iloc[:,[3,4]].values      
                                Y=dataset.iloc[:,[16]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,4]].values      
                                Y1=dataset1.iloc[:,[16]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("resultffff.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('resultffff.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(1))
                                
                else:
                        print('THE SUM OF ALL PLAYERS SHOULD BE 11')
        
                
                        

            elif y==2:
                print('odi')
                print('=====================ODI=====================')
                
                
                
                c=int(input('1.ENTER THE NUMBER OF BATSMAN'))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS'))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS'))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('enter your choice'))
                            if a==1:
                        
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('aus_odi1.csv')
                                
                                X=dataset.iloc[:,[3,4,5,6]].values      
                                Y=dataset.iloc[:,[8]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,4,5,6]].values      
                                Y1=dataset1.iloc[:,[8]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("resultodi1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('resultodi1.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('BOWLER')
                        
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('aus_odi1.csv')
                                
                                X=dataset.iloc[:,[3,9,10]].values      
                                Y=dataset.iloc[:,[12]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,9,10]].values      
                                Y1=dataset1.iloc[:,[12]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("resultodi2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('resultodi2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print('BOWLERS')
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('WICKETKEPPER')
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('aus_odi1.csv')
                                
                                X=dataset.iloc[:,[3,4]].values      
                                Y=dataset.iloc[:,[16]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,4]].values      
                                Y1=dataset1.iloc[:,[16]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("resultodi3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('resultodi3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(1))
                                
                else:
                        print('THE SUM OF ALL PLAYERS SHOULD BE 11')

            elif y==3:
                
                print('=====================TEST=====================')
                
                
                
                c=int(input('1.ENTER THE NUMBER OF BATSMAN'))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS'))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS'))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('enter your choice'))
                            if a==1:
                        
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('austest.csv')
                                
                                X=dataset.iloc[:,[3,4,5,6]].values      
                                Y=dataset.iloc[:,[8]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,4,5,6]].values      
                                Y1=dataset1.iloc[:,[8]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("resulttest1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('resulttest1.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('BOWLER')
                        
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('austest.csv')
                                
                                X=dataset.iloc[:,[3,9,10]].values      
                                Y=dataset.iloc[:,[12]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,9,10]].values      
                                Y1=dataset1.iloc[:,[12]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("resulttest2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('resulttest2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print('BOWLERS')
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('WICKETKEPPER')
                                
                                #def test2(x):
                                 #   x=2
                                #importing dataset
                                dataset=pd.read_csv('austest.csv')
                                
                                X=dataset.iloc[:,[3,4]].values      
                                Y=dataset.iloc[:,[16]].values
                                
                                #splitting the dataset into training set and test set
                                
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                dataset1=pd.read_csv('Book2.csv')
                                X1=dataset1.iloc[:,[3,4]].values      
                                Y1=dataset1.iloc[:,[16]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("resulttest3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('resulttest3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(1))
                                

            elif y==4:
                break
                


    elif x==3:
        for i in range(0,3):
            print('1.T20')
            print('2.ODI')
            print('3.TEST')
            print('4.EXIT')
            y=int(input('ENTER THE FORMAT'))
            if y==1:
                print('T20')
            
                print('=================PLAYING 11 PREDICTION FOR T-20 MATCH==================')
                print('ENGLAND T-20')
                #Importing libraries
                
                
                #Importing the dataset of test match
                dataset=pd.read_csv('eng_t20.csv')
                
                c=int(input('1.ENTER THE NUMBER OF BATSMEN : '))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS : '))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS : '))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('Among the three, which do u want to select : '))
                            if a==1:
                                print('*******')
                                print('BATSMEN')
                                print('*******')
                                
                                X=dataset.iloc[:,[4,5]].values      
                                Y=dataset.iloc[:,[7]].values
                                
                                #splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('t20_testdata.csv')
                                X1=dataset1.iloc[:,[4,5]].values      
                                Y1=dataset1.iloc[:,[7]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("result1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('result1.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('*******')
                                print('BOWLERS')
                                print('*******')
                                
                                X=dataset.iloc[:,[4,8,9]].values      
                                Y=dataset.iloc[:,[11]].values
                                
                                #Splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('t20_testdata.csv')
                                X1=dataset1.iloc[:,[4,8,9]].values      
                                Y1=dataset1.iloc[:,[11]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("result2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('result2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('*******')
                                print('WICKETKEEPERS')
                                print('*******')
                                
                                X=dataset.iloc[:,[9,12]].values      
                                Y=dataset.iloc[:,[13]].values
                                
                                #splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('t20_testdata.csv')
                                X1=dataset1.iloc[:,[9,12]].values      
                                Y1=dataset1.iloc[:,[13]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("result3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('result3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(e))
                                
                else:
                        print('THE SUM OF ALL PLAYERS SHOULD BE 11')
        



            elif y==2:
                print('ODI')
                print('==========PLAYING 11 PREDICTION FOR ONE DAY INTERNATIONAL MATCH============')
                print('ENGLAND ODI')
                #Importing libraries
                
                
                #Importing the dataset of test match
                dataset=pd.read_csv('england_odi.csv')
                
                c=int(input('1.ENTER THE NUMBER OF BATSMEN : '))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS : '))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS : '))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('Among the three, which do u want to select : '))
                            if a==1:
                                print('*******')
                                print('BATSMEN')
                                print('*******')
                                
                                X=dataset.iloc[:,[4,5]].values      
                                Y=dataset.iloc[:,[7]].values
                                
                                #splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('odi_testdata.csv')
                                X1=dataset1.iloc[:,[4,5]].values      
                                Y1=dataset1.iloc[:,[7]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("result1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('result1.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('*******')
                                print('BOWLERS')
                                print('*******')
                                
                                X=dataset.iloc[:,[4,8,9]].values      
                                Y=dataset.iloc[:,[11]].values
                                
                                #Splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('odi_testdata.csv')
                                X1=dataset1.iloc[:,[4,8,9]].values      
                                Y1=dataset1.iloc[:,[11]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("result2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('result2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('*******')
                                print('WICKETKEEPERS')
                                print('*******')
                                
                                X=dataset.iloc[:,[9,12]].values      
                                Y=dataset.iloc[:,[13]].values
                                
                                #splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('odi_testdata.csv')
                                X1=dataset1.iloc[:,[9,12]].values      
                                Y1=dataset1.iloc[:,[13]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("result3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('result3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(e))
                                
                else:
                        print('THE SUM OF ALL PLAYERS SHOULD BE 11')
                        
                
                

            elif y==3:
                print('TEST')
                
                print('=====================PLAYING 11 PREDICTION FOR TEST MATCH=====================')
                print('ENGLAND TEST')
                #Importing libraries
                
                
                #Importing the dataset of test match
                dataset=pd.read_csv('eng_test.csv')
                
                c=int(input('1.ENTER THE NUMBER OF BATSMEN : '))
                d=int(input('2.ENTER THE NUMBER OF BOWLERS : '))
                e=int(input('3.ENTER THE NUMBER OF WICKETKIPPERS : '))
                
                f=c+d+e
                if f==11:
                    for i in range(0,3):    
                            a=int(input('Among the three, which do u want to select : '))
                            if a==1:
                                print('*******')
                                print('BATSMEN')
                                print('*******')
                                
                                X=dataset.iloc[:,[4,5]].values      
                                Y=dataset.iloc[:,[7]].values
                                
                                #splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('test_testdata.csv')
                                X1=dataset1.iloc[:,[4,5]].values      
                                Y1=dataset1.iloc[:,[7]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Avg']=Y_predict
                                
                                dataset1.to_csv("result1.csv", columns=['Cap','Name','Avg'], index=False)
                                
                                dataset2=pd.read_csv('result1.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(c))
                           
                            elif a==2:
                                print('*******')
                                print('BOWLERS')
                                print('*******')
                                
                                X=dataset.iloc[:,[4,8,9]].values      
                                Y=dataset.iloc[:,[11]].values
                                
                                #Splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('test_testdata.csv')
                                X1=dataset1.iloc[:,[4,8,9]].values      
                                Y1=dataset1.iloc[:,[11]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['Wkt']=Y_predict
                                
                                dataset1.to_csv("result2.csv", columns=['Cap','Name','Wkt'], index=False)
                                
                                dataset2=pd.read_csv('result2.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(d))        
                             
                                
                            elif a==3:
                                print('*******')
                                print('WICKETKEEPERS')
                                print('*******')
                                
                                X=dataset.iloc[:,[9,12]].values      
                                Y=dataset.iloc[:,[13]].values
                                
                                #splitting the dataset into training set and test set
                                
                                X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3,random_state=0)
                                
                                
                                #Fitting simple linear Regression to the training set
                                
                                regressor = LinearRegression()
                                regressor.fit(X_train,Y_train)
                                
                                #Importing the test dataset
                                dataset1=pd.read_csv('test_testdata.csv')
                                X1=dataset1.iloc[:,[9,12]].values      
                                Y1=dataset1.iloc[:,[13]].values
                                Y_predict=regressor.predict(X1)    
                                dataset1['St']=Y_predict
                                
                                dataset1.to_csv("result3.csv", columns=['Cap','Name','St'], index=False)
                                
                                dataset2=pd.read_csv('result3.csv')
                                X3=dataset2.iloc[:,:].values
                                
                                
                                df = pd.DataFrame(X3)
                                result = df.sort_values(by=2,ascending=False)
                                print(result.head(e))
                            

            elif y==4:
                break
                
    elif x==4:
        break
 


# In[24]:



x=py()


# In[26]:





# In[27]:


pickle.dump(py(),open('model.pkl','wb'))


# In[16]:


pickled_model=pickle.load(open('model.pkl','rb')


# In[18]:


py()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




