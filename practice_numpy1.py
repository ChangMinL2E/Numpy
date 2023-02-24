import numpy as np

a = [[1,2,3],[4,5,6]]
b = np.array(a)
print(b) # [[1,2,3],[4,5,6]]

print(b.ndim) # 배열의 차원

print(b[0,0]) # b[0][0]과 똑같다.

## 특수한 배열의 생성

lst1 = np.arange(10)
print(lst1) # [0,1,2,3,4,5,6,7,8,9]

lst2 = np.arange(5,10)
print(lst2) # [5,6,7,8,9]

lst3 = np.arange(5,10,3)
print(lst3) # [5,8]

lst_zeros = np.zeros((2,2))
print(lst_zeros) # 2x2 0행렬

lst_ones = np.ones((2,3))
print(lst_ones) # 2x3 원소가 1인 행렬

lst_full = np.full((2,3),5)
print(lst_full) # 2x3 원소가 5인 행렬

identity_Matrix = np.eye(3) # 3차원 단위행렬
print(identity_Matrix)

## 배열의 차원 변환

a = np.arange(20)
b = a.reshape((4,5))
print(b)

# concatenate 이어붙이기
x = np.array([0,1,2])
y = np.array([3,4,5])
print(np.concatenate([x,y])) # [0,1,2,3,4,5]

# concatenate 행렬통째로 이어붙이기
x = np.array([[1,2],[3,4]])
y = np.array([[1,2],[3,4]])
print(np.concatenate([x,y],axis=1)) # 기본으로 세로로 붙는다. axis=1로 가로로 연결할수도 있다.

# split 행렬 axis 축 기준으로 분할
matrix = np.arange(16).reshape(4,4)
upper, lower = np.split(matrix, [3], axis=0)
print(upper, lower) 

## 브로드캐스팅
matrix = np.array([[2,4,2],[6,5,9],[9,4,7]])
matrix2 = np.array([1,2,3])
print(matrix+matrix2)

array1 = np.arange(3).reshape((3,1))
array2 = np.arange(3)
print(array1+array2)

# 집계 & 마스킹연산
x = np.arange(5)

print(x < 3) # [True, True, True, False, False]

print(x[x<3]) # [0,1,2]
