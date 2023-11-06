# person.py

class Person:
    def __init__(self, n, a):
        self.name = n       # 이름 정보
        self.age = a       # 나이 정보

    def __str__(self):
        return '{0}: {1}'.format(self.name, self.age)


def main():
    p = Person('James', 22)       # 22살의 James
    print(p)
    p.age -= 1    # 나이 한 살 더 먹어서 넣은 문장
    print(p)

main()
