# vector_inp1.py

class Vector:     
    def __init__(self, x, y):
        self.x = x       
        self.y = y       
        
    def __add__(self, o):    # 벡터의 덧셈 연산
        return Vector(self.x + o.x, self.y + o.y)
 
    def __str__(self):      # 벡터 정보를 문자열로 반환
        return 'Vector({0}, {1})'.format(self.x, self.y)


def main():
    v1 = Vector(2, 2)
    v2 = Vector(7, 7)

    print(v1, id(v1))
    v1 += v2       # v1 = v1.__add__(v2)
    print(v1, id(v1))

main()
