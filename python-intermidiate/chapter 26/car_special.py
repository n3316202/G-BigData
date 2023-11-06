# car_special.py

class Car:
    def __init__(self, id):
        self.id = id       # 차량 번호


    def __len__(self):
        return len(self.id)      # 차량 번호의 길이가 반환됨

    def __str__(self):
        return 'Vehicle number : ' + self.id


def main():
    c = Car("32러5234")
    print(len(c))
    print(str(c))

main()
