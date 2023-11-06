# count_instance2.py

class Simple:
    count = 0
    
    def __init__(self):
        Simple.count += 1
        
    @staticmethod
    def get_count():
        return Simple.count


def main():
    print(Simple.get_count())
    s = Simple()
    print(Simple.get_count())

main()
