# overloading.py

class Account:     # 계좌 클래스
    def __init__(self, aid, abl):
        self.aid = aid       # 계좌 번호
        self.abl = abl       # 계좌 잔액
        
    def __add__(self, m):    # 입금
        self.abl += m
        print('__add__')

    def __sub__(self, m):     # 인출
        self.abl -= m
        print('__sub__')

    def __call__(self):      # 계좌 상황을 문자열로 반환
        print('__call__')
        return str(self.aid) + ':' + str(self.abl)


def main():
    acnt = Account('James01', 100)     # 계좌 개설
    acnt + 100     # 100원 입금
    # acnt.__add__(100)
    
    acnt - 50      # 50원 인출
    # acnt.__sub__(50)
    
    print(acnt())
    # print(acnt.__call__())

main()
