import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(5,2), columns=["A","B"])
# print(df["A"] < 0.5)
# print(df[(df["A"]<0.5) & (df["B"]>0.3)])
# print(df.query("A<0.5 & B>0.3"))

df = pd.DataFrame({
    "Animal" : ['Dog', 'Cat', 'Cat', 'Pig','Cat'],
    "Name" : ['Happy', 'Sam','Toby','Mini','Rocky']
})
# print(df["Animal"].str.contains("Cat"))
# print(df.Animal.str.match("Cat"))

df = pd.DataFrame(np.arange(5), columns=["Num"])
# print(df["Num"].apply(lambda x: x**2))
df["Square"] = df.Num.apply(lambda x: x**2)
# print(df)

df = pd.DataFrame(columns=["phone"])
df.loc[0] = "010-1234-1234"
df.loc[1] = "공일공-일이삼사-사삼이일"

# df["preprocess_phone"] = ''

dic = {
    "공":"0",
    "일":'1',
    "이":'2',
    "삼":'3',
    "사":'4',
    "-":'',
    ".":""
}

def func(x):
    for a, b in dic.items():
        x = x.replace(a,b)
    return x
# df["preprocess_phone"] = df["phone"].apply(func)
# print(df.replace({"010-1234-1234":"안녕하세요", "공일공-일이삼사-사삼이일":"저에요"}))

df = pd.DataFrame({'key':["a",'b','c',"a",'b','c'], 'data1':[1,2,3,1,2,3],'data2':[1,3,4,5,6,7]})
# print(df.groupby('key'))
# print(df.groupby('key').sum())
# print(df.groupby(['key','data1']).sum())

# print(df.groupby('key').aggregate(['min',np.median,max]))
# print(df.groupby('key').aggregate({'data1':"min", 'data2':np.sum}))

# print(df.groupby('key').filter(lambda x: x['data2'].mean()>3))
# print(df.groupby('key').apply(lambda x: x.max()- x.min()))

df = pd.DataFrame(
    np.random.randn(4,2),
    index=[['A','A','B','B'],[1,2,1,2]],
    columns=['data1','data2']
)
df = pd.DataFrame(
    np.random.randn(4,4),
    columns=[['A','A','B','B'],[1,2,1,2]],
)
# print(df)

df = pd.DataFrame(
    {
    'A':[0,1,2,3,4],
    'B':[0,1,2,3,4],
    'C':[0,1,2,3,4],
    'D':[0,1,2,3,4],
    'E':[0,1,2,3,4],
    }
)

print(df.pivot_table(
    index='A',columns="B",values="C",
    # aggfunc=np.mean
))