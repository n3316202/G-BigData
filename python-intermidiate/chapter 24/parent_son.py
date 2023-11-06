# parent_son.py

class Father:
    def run(self):
        print("so fast!!!")

class Mother:
    def dive(self):
        print("so deep!!")

class Son(Father, Mother):
    def jump(self):
        print("so high!!!")

def main():
    s = Son()
    s.run()
    s.dive()
    s.jump()

main()
