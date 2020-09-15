import pandas as pd


df = pd.read_csv('dataset.csv')

print(df)

df2 = df[df['x1']<0]

print(df2)


x_variables = df.iloc[:,0:30]

print(x_variables)

y_variable = df.iloc[:,30]

print(y_variable)



