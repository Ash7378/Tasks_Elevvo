import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


data = pd.read_csv('C:\\Users\\AHMED 1\\Desktop\\Elevvo\\titanic\\train.csv')
sb.set_theme(style="dark")

#data visualization
#Survival count By gender
sb.countplot(data=data, x='Sex',hue='Survived')
plt.title('Survival Count By Gender')
plt.xticks(ticks=[0, 1], labels=['0=NO', '1=YES'])

plt.show ()

#Survival by Passenger class
sb.barplot(data=data, x='Pclass',y='Survived')
plt.xticks(ticks=[0, 1, 2], labels=['Upper', 'Middle', 'Lower'])
plt.title('Survival rate By Passenger Class')
plt.show ()

#Age distribution of survivors Vs Non Survivors
sb.histplot(data=data,x='Age',hue='Survived',multiple='stack')
plt.title("Age Distribution By Survival")
plt.show()

#Correlation
cor= data.corr(numeric_only=True)
sb.heatmap(cor,annot=True,cmap='viridis',fmt=".2f")
plt.show()