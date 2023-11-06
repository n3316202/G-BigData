# person4.py

class Person:
    def __init__(self, n, a):
        self._name = n       # 이름 정보
        self._age = a       # 나이 정보

    def add_age(self, a):
        if(a < 0):
            print('나이 정보 오류')
        else:
            self._age += a

    def __str__(self):
        return '{0}: {1}'.format(self._name, self._age)


def main():
    p = Person('James', 22)       # 22살의 James
    # p._age += 1     # 이렇게 안쓰기로 약속했다.
    p.add_age(1)
    print(p)

main()
