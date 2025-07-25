#Creating Heatmap Survival rates by ---> sex and class
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#loading the data
data = pd.read_csv('C:\\Users\\AHMED 1\\Desktop\\Elevvo\\titanic\\train.csv')
pivot=data.pivot_table('Survived', index='Sex', columns='Pclass')
sb.heatmap(pivot, annot=True,cmap='Blues')

plt.title("Survival rate by Gender and Classs")
plt.show()