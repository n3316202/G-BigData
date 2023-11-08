#https://datascienceschool.net/01%20python/03.05%20%EB%82%9C%EC%88%98%20%EB%B0%9C%EC%83%9D%EA%B3%BC%20%EC%B9%B4%EC%9A%B4%ED%8C%85.html
#3.5 난수 발생과 카운팅

import numpy as np

np.random.seed(0)
r = np.random.rand(5)
print(r)

r = np.random.rand(10)
print(r)
