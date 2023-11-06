# class_method2.py

class Simple:
    count = 0

    def __init__(self):
        Simple.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
        
def main():
    print(Simple.get_count())
    s = Simple()
    print(Simple.get_count())
    

main()
