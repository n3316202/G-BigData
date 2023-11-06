# father_son3.py

class Father:
    def run(self):
        print("so fast, dad style")

class Son(Father):
    def run(self):
        print("so fast, son style")

    def run2(self):
        super().run()

def main():
    s = Son()
    s.run()
    s.run2()

main()
