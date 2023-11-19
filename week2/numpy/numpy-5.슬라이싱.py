#https://076923.github.io/posts/Python-numpy-5/

import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a)
print(a[3:])
print(a[1:-1]) #-1을 입력할 경우, 마지막 index-1 (len-2)를 의미합니다.
print(a[0:3:2])

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

print(a)
print(a[:, 1:])
print(a[0:1,0:2])

import numpy as np

a = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]])

print(a)
print(a[::2, ::2])