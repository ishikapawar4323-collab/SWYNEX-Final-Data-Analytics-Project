import pandas as pd

df=pd.read_csv('Titanic_Raw.csv')
df=df.drop_duplicates()
df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Cabin']=df['Cabin'].fillna('Unknown')
df['Sex']=df['Sex'].str.strip().str.lower()
df['Embarked']=df['Embarked'].str.strip().str.upper()
df.to_csv('Titanic_Cleaned.csv',index=False)
print('Cleaning completed successfully!')
