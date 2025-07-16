
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#loading the data
data = pd.read_csv('C:\\Users\\AHMED 1\\Desktop\\Elevvo\\titanic\\train.csv')
data.head()
data.info()
data.describe()
data.isnull().sum()

#Cleaning data #as example
data.fillna({
    'Age':data['Age'].median(),'Embarked':
    data['Embarked'].mode()[0]},
    inplace=True)
data.drop('Cabin',axis=1,inplace=True)

#Summary Statistics and Group insights
data['Survived'].value_counts(normalize=True) #overall survival rate
data.groupby('Sex')['Survived'].mean()  #By gender
data.groupby('Pclass')['Survived'].mean() #by passengerclass

data.pivot_table('Survived',index='Sex',columns='Pclass')
data.to_csv('clean_titanic_data.csv',index=False)


