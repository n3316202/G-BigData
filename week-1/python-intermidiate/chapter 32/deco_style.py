# deco_style.py

def adder_deco(func):       # 데코레이터 함수
    def ad(*args):
        print(*args, sep = ' + ', end = ' ')
        print("= {0}".format(func(*args)))
    return ad


@adder_deco
def adder2(n1, n2):       # 전달 인자가 두 개인 함수
    return n1 + n2

@adder_deco
def adder3(n1, n2, n3):       # 전달 인자가 세 개인 함수
    return n1 + n2 + n3


def main():
    adder2(3, 4)
    adder3(3, 5, 7)

main()
