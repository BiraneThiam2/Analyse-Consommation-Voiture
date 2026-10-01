import pandas as pd
df=pd.read_csv('mpg.csv')

#Diagnostic
df.info()
print(df.describe())
print(df.duplicated().sum())

#Nettoyage des données
df['horsepower']=df['horsepower'].fillna(df['horsepower'].median())
print(df.isna().sum())

#Analyse des données
print("La consommation moyenne mpg est de :")
print(df['mpg'].mean())

print("La consommation moyenne mpg par origine est de :")
print(df.groupby('origin')['mpg'].mean())

print("Le poids moyen par origine est de :")
print(df.groupby('origin')['weight'].mean())

print("La consommation moyenne mpg par nombre de cylindres est de :")
print(df.groupby('cylinders')['mpg'].mean())

df['recente']=df['model_year'] >= 76
print("La consommation moyenne mpg des véhicules récents est de :")
print(df.groupby('recente')['mpg'].mean())

print("La consommation moyenne mpg par origine et par récence est de :")
print(df.groupby(['origin', 'recente'])['mpg'].mean())
print(df.sort_values('mpg', ascending=False).head(1))

