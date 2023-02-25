import pandas as pd
import numpy as np

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

Ser3 = nameDF['tall']/nameDF['order']
nameDF['div'] = Ser3

# print(nameDF.loc['LCM':'SJH','tall':'order'])

# print(nameDF.iloc[0:3, :2])

DF = pd.DataFrame(columns=['A','B','C'])
DF.loc[0] = ['one','two','three']
DF.loc[1] = {'A':'에이','B':'비','C':'씨'}
DF.loc[1,'A'] = "애이"

DF['call'] = np.nan
DF.loc[0,'call'] = '01034341234'
# print(DF)
# print(len(DF))

## 연산과 함수
# print(DF.isnull())
# print(DF.notnull())


# print(DF.dropna())
DF['call'] = DF['call'].fillna('전화번호 없음')
# print(DF)

A = pd.Series([2,4,6], index=[0,1,2])
B = pd.Series([1,3,5], index=[1,2,3])
# print(A+B)

# print(A.add(B, fill_value=0))

A = pd.DataFrame(np.random.randint(0,10,(2,2)), columns=list("AB"))
B = pd.DataFrame(np.random.randint(0,10,(3,3)), columns=list("BAC"))
# print(A+B)

data = {
  'A': [i+5 for i in range(3)],
  'B' : [i**2 for i in range(3)]
}
DF = pd.DataFrame(data)
# print(DF['A'].sum()) # 18
# print(DF.sum())
# print(DF.mean())

df = pd.DataFrame({
  'col1' : [2,1,9,8,7,4],
  'col2' : ['A','A','B',np.nan, 'D','C'],
  'col3' : [0,1,9,4,2,3]
})

print(df.sort_values(['col2','col1']))