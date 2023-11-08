#배열의 생성과 변형
#https://datascienceschool.net/01%20python/03.02%20%EB%B0%B0%EC%97%B4%EC%9D%98%20%EC%83%9D%EC%84%B1%EA%B3%BC%20%EB%B3%80%ED%98%95.html

import numpy as np

x = np.array([1, 2, 3])
print(np.dtype)

#Inf와 NaN
#넘파이에서는 무한대를 표현하기 위한 np.inf(infinity)와 정의할 수 없는 숫자를 나타내는
# np.nan(not a number)을 사용

print(np.array([0, 1, -1, 0]) / np.array([1, 0, 0, 0]))