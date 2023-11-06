# prt_dict.py

class Simple:
    def __init__(self, n, s):
        self._n = n       # 단순 정수
        self._s = s       # 단순 문자열

    def __str__(self):
        return '{0}: {1}'.format(self._n, self._s)


def main():
    sp = Simple(10, 'my')
    print(sp)

    sp.__dict__['_n'] += 10
    sp.__dict__['_s'] = 'your'
    print(sp)

main()
