# car_iterable.py

class Car:
    def __init__(self, id):
        self.id = id       # 차량 번호


    def __iter__(self):
        return iter(self.id)


def main():
    c = Car("32러5234")
    for i in c:
        print(i, end = ' ')
    

main()
