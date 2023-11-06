# person_dict2.py

class Person:
    def __init__(self, n, a):
        self._name = n       # 이름 정보
        self._age = a       # 나이 정보

def main():
    p = Person('James', 22)       # 22살의 James
    print(p.__dict__)
    p.len = 178
    p.adr = 'Korea'
    print(p.__dict__)

main()
