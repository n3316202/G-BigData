# natural6.py

class Natural:       # 자연수를 표현한 클래스
    def __init__(self, n):
        self.n = n       # 프로퍼티 n을 통해 접근

    @property
    def n(self):
        return self.__n
    
    @n.setter    
    def n(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n


def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    
    n1.n = n2.n + n3.n
    print(n1.n)
    
main()
