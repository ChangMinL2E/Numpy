import numpy as np

# 인덱싱 슬라이싱
lst = np.array([[1,2,3],[4,5,6],[7,8,9]])

slicing_lst = lst[:2,:2]
print(slicing_lst) # [[1,2],[4,5]]
print(lst[1]) # [4,5,6]


## 연산

a = np.array([1,2,3])
b = np.array([4,5,6])

# 각 요소 더하기
c = a+b # c = add(a,b)
print(c) # [5,7,9]

# 각 요소 곱하기 np.multiply(a,b)
print(a*b) # [4,10,18] 

# 각 요소 나누기 np.divide(a,b)
print(a/b) # [0.25, 0.4, 0.5]

# 행렬곱 np.dot

arr1 = [[1,2],[3,4]]
arr2 = [[5,6],[7,8]]
a = np.array(arr1)
b = np.array(arr2)

c = np.dot(a,b)
print(c) # [[19 22] [43 50]]

# 모든 원소의 합, 곱 sum(), prod()
a = np.array([[-1,2,3],[3,4,8]])
print(np.sum(a)) # 19
print(np.sum(a,axis=0)) # [2 6 11]

print(a.mean()) # 3.1666... mean
print(a.std()) # 2.671... standard
print(a.prod()) # -576 product


