
# ALIAS DEL NOME NON C'è DIFFERENZA 

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(myvar.loc[0 , 1])
# per poter localizare un elemento in un dataframe abbiamo bisogno di .loc e delle []

df = pd.DataFrame(mydataset, index =  ["mia macchina"," macchina mamma"])
 
print(df)

##print(pd.__version__)


a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["z"])



calories = {"day1": 420, "day2": 380, "day3": 390}

myvar2 = pd.Series(calories, index = ["day1" ,"day2" ])

print(myvar2)



# può essere letto e inserito all'interno di un dataframe
df = pd.read_csv("x.csv") #nomex
print(df.to_string())   # con il to_string possiamo stampare l'intero dataframe


df = pd.read_json('data.json') #nomex
print(df.to_string()) 