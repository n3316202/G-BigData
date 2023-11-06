# natural.py

class Natural:       # 자연수를 표현한 클래스
    def __init__(self, n):
        if(n < 1): 
            self.__n = 1
        else:
            self.__n = n

    def getn(self):
        return self.__n
    def setn(self, n):
        if(n < 1):
            self.__n = 1
        else:
            self.__n = n


def main():
    n = Natural(-3)
    print(n.getn())
    
    n.setn(2)
    print(n.getn())

main()
