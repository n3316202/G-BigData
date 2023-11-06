# car.py

class Car:
    def __init__(self, id, f):
        self.id = id       # 차량 번호
        self.fuel = f       # 연료 정보

    def drive(self):
        self.fuel -= 10       # 주행 시 연료 감소

    def add_fuel(self, f):       # 연료 보충
        self.fuel += f

    def show_info(self):       # 현재 차의 상태
        print("id:", self.id)
        print("fuel:", self.fuel)


def main():
    c = Car("32러5234", 0)      # 자동차 구매 및 등록
    c.add_fuel(100)     # 연료 보충
    c.drive()       # 주행
    c.show_info()       # 지금 차량 상태는?

main()
