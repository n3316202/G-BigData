# person_dict3.py

class Person:
    def __init__(self, n, a):
        self.__name = n       # 이름 정보
        self.__age = a       # 나이 정보

def main():
    p = Person('James', 22)       # 22살의 James
    print(p.__dict__)

main()
