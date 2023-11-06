# person3.py

class Person:
    def __init__(self, n, a):
        self.__name = n       # 이름 정보
        self.__age = a       # 나이 정보

    def add_age(self, a):
        if(a < 0):
            print('나이 정보 오류')
        else:
            self.__age += a

    def __str__(self):
        return '{0}: {1}'.format(self.__name, self.__age)


def main():
    p = Person('James', 22)       # 22살의 James
    # p.__age += 1     # 이 문장을 실행하면 오류가 발생함
    p.add_age(1)
    print(p)

main()
