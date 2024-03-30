import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Student_marks.csv')

average=df['Marks'].mean()
hm=df['Marks'].max()
lm=df['Marks'].min()

print("the overview of the Marks(highest, lowest, average) of the students is below:")
print("Highest Marks : ", hm)
print("Lowest Marks  : ", lm)
print("Average Marks : ", average)

a=b=c=d=f=0

grade=[]
for i in range(len(df)):
    if df['Marks'][i] >=50:
        grade.append('A')
        a+=1
    elif (df['Marks'][i] >=40) and (df['Marks'][i]<50):
        grade.append('B')
        b+=1
    elif (df['Marks'][i] >=30) and (df['Marks'][i]<40):
        grade.append('C')
        c+=1
    elif (df['Marks'][i] >=18) and (df['Marks'][i]<30):
        grade.append('D')
        d+=1
    else :
        grade.append('F')
        f+=1

y = np.array([a, b, c, d, f])
mylabels = ["A", "B", "C", "D","F"]
mycolors= ["green","blue","yellow", "orange", "red"]

plt.pie(y, labels = mylabels, colors=mycolors)
plt.show()
