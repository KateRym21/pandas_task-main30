import pandas as pd

df = pd.read_csv('GoogleApps.csv')

print(df.info())
#print(df.head(1))
#print(df.tail())
#print(df.describe())
print(df[df["Rating"]>4.9]["Installs"].mean())

print(df[df["Type"]=="Paid"]["Price"].min())
print(df[df["Type"]=="Paid"]["Price"].min())
print(df[df["Category"] == "ART_AND_DESIGN"]["Installs"].median())

free = df[df['Type']=="Free"]["Reviews"].max()
paid = df[df['Type']=="Paid"]["Reviews"].max()
print(free-paid)

temp = df.groupby(by = 'Type')
['Rating'].mean()

print(round(temp['Paid'] - temp['Free'],2))
print(round(temp,2))

temp = df.groupby(by = 'Category')
['Size'].agg([min,max,mean,median])
print(temp)

print(round(df.groupby(by = 'Type')['Rating'].agg(['min','mean','max']),1))

print(df[df['Type'] =='Paid'].groupby(by = 'Content Rating')
['Price'].agg([min, median, max]))
print("__________________________________________________")
print(df.pivot_table(columns = 'Type,'index = 'Content Rating',values= 'Size,aggfunc = ''min'))

temp = df.pivot_table(index = 'Content Rating', columns = 'Category', values = 'Reviews',aggfunc ='max')
print(temp)
print(temp[['EDUCATION', 'FAMILY','GAME']])




