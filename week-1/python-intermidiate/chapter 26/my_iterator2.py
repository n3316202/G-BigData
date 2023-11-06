# my_iterator2.py

class Coll2:
    def __init__(self, d):
        self.ds = d
        
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration

        self.cc += 1
        return self.ds[self.cc - 1]

    def __iter__(self):
        self.cc = 0      # next 호출 횟수 초기화
        return self      # 이 객체를 그대로 반환함


def main():
    co = Coll2([1, 2, 3, 4, 5])

    for i in co:
        print(i, end = ' ')
        
    for i in co:
        print(i, end = ' ')

main()
