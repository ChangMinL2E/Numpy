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


print(DF.dropna())
DF['call'] = DF['call'].fillna('전화번호 없음')
print(DF)