import numpy as np
#수치해석 빠른 성능좋은 배열 array : numpy

arr = np.arange(10)
print(arr)
print(type(arr))


arr = np.random.normal(5,3,500) #전체 평균수, 표준편차, 표준수
print(arr)


#평균
print(arr.mean())

#합계
print(arr.sum())

#표준편차
print(arr.std())

#분산
print(arr.var())

#최대값
print(arr.max())

# 최대값 , 최소값위치
print(arr.argmax(), arr.argmin())

