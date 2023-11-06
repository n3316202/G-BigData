# static_method.py

class Simple:
    # @staticmethod
    def sm():
        print('static method!')

    sm = staticmethod(sm)


def main():
    Simple.sm()
    s = Simple()
    s.sm()

main()
