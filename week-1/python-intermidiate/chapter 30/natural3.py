# natural3.py

class Natural:       # 자연수를 표현한 클래스
    def __init__(self, n):
        self.setn(n)       # 아래에 있는 setn 메소드 호출

    def getn(self):
        return self.__n
    
    def setn(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n

    n = property(getn, setn)


def main():
    n1 = Natural(1)
    n2 = Natural(2)
    n3 = Natural(3)
    
    n1.n = n2.n + n3.n     # n2와 n3의 덧셈 결과를 n1에 저장
    print(n1.n)
    
main()
