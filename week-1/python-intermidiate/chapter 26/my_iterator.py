# my_iterator.py

class Coll:
    def __init__(self, d):
        self.ds = d
        self.cc = 0       # next 호출 횟수
        
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration

        self.cc += 1
        return self.ds[self.cc - 1]


def main():
    co = Coll([1, 2, 3, 4, 5])    # 튜플 및 문자열도 전달할 수 있음

    while True:
        try:
            i = next(co)      # iterator 객체를 통해서 하나씩 꺼낸다.
            print(i, end = ' ')
        except StopIteration:      # 더 이상 꺼낼 객체가 없으면,
            break      # 이 루프를 탈출한다.
    

main()
