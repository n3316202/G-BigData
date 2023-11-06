# account.py

class Account:     # 계좌 클래스
    def __init__(self, aid, abl):
        self.aid = aid       # 계좌 번호
        self.abl = abl       # 계좌 잔액
       
    def __iadd__(self, m):       # 입금
        self.abl += m
        return self

    def __isub__(self, m):       # 출금
        self.abl -= m
        return self

    def __str__(self):      # 계좌 상황을 문자열로 반환
        return '{0}, {1}'.format(self.aid, self.abl)


def main():
    acnt = Account('James01', 100)     # 계좌 개설
    acnt += 130     # 130원 입금
    print(acnt)
    acnt -= 50      # 50원 출금
    print(acnt)

main()
