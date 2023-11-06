# deco_style2.py

def deco1(func):       # 데코레이터 1
    def inner():
        print('deco1')
        func()
    return inner

def deco2(func):       # 데코레이터 2
    def inner():
        print('deco2')
        func()
    return inner

@deco1
@deco2
def simple():
    print('simple')


def main():
    simple()

main()
