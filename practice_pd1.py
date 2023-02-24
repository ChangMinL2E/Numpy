import pandas as pd

## Series
data = pd.Series([1,2,3,4])
# print(data)

data = pd.Series([1,2,3,4],index=['a','b','c','d'])
# print(data)

data = pd.Series([1,2,3,4],index=['a','b','c','d'], name="시리즈")
data['c'] = 5
# print(data)

dict = {
    'LCM' : 178,
    'SJH' : 207,
    'HJW' : 175
}

Ser = pd.Series(dict)
# print(dict,"\n", Ser)

## DataFrame

dict1 = {
    'LCM' : 178,
    'SJH' : 207,
    'HJW' : 175
}

dict2 = {
  'LCM' : 1,
  'SJH' : 2,
  'HJW' : 3
}

Ser1 = pd.Series(dict1)
Ser2 = pd.Series(dict2)
nameDF = pd.DataFrame({
    'tall' : Ser1,
    'order' : Ser2 
})

# print(nameDF)
# print(nameDF.index)
# print(nameDF.columns)
# print(nameDF['tall'])
Ser3 = nameDF['tall']/nameDF['order']
nameDF['div'] = Ser3
# print(nameDF)

# nameDF.to_csv("./first.csv")
# printDF = pd.read_csv('./first.csv')
# print(printDF)