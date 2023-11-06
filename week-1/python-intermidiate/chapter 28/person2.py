# person2.py

class Person:
    def __init__(self, n, a):
        self.name = n       # 이름 정보
        self.age = a       # 나이 정보

    def add_age(self, a):
        if(a < 0):
            print('나이 정보 오류')
        else:
            self.age += a

    def __str__(self):
        return '{0}: {1}'.format(self.name, self.age)


def main():
    p = Person('James', 22)       # 22살의 James
    p.add_age(1)
    print(p)

main()
