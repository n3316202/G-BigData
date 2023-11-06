# truck.py

class Car:
    def __init__(self, id, f):
        self.id = id       
        self.fuel = f      

    def drive(self):
        self.fuel -= 10     

    def add_fuel(self, f):  
        self.fuel += f

    def show_info(self):
        print("id:", self.id)
        print("fuel:", self.fuel)

class Truck(Car):
    def __init__(self, id, f, c):
        super().__init__(id, f)
        self.cargo = c

    def add_cargo(self, c):
        self.cargo += c

    def show_info(self):       # 현재 차의 상태
        super().show_info()
        print("cargo:", self.cargo)


def main():
    t = Truck("42럭5959", 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()

main()
