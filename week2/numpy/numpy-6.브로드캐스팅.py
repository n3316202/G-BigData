#https://076923.github.io/posts/Python-numpy-12/
#https://velog.io/@kungsboy/Numpy-%EB%B8%8C%EB%A1%9C%EB%93%9C%EC%BA%90%EC%8A%A4%ED%8C%85
import numpy as np

array1 = np.array([1, 2, 3, 4]).reshape(2, 2)
array2 = np.array([1.5, 2.5])

add = array1 + array2

print(add)

import numpy as np

Value = np.array([[1, 2, 3, 4], [2, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
Value1 = np.array([1])
Value2 = np.array([3, 3, 3, 3])
Value3 = np.array([4, 5, 6, 7]).reshape(4, 1)
print(Value3)
#print(Value + Value1)  # 4x4 + 1
#print(Value + Value2)  # 4x4 + 1x4
print(Value2 + Value3)  # 1x4 + 4x1
