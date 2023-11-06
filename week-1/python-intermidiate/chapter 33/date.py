# date.py

class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print('{0}, {1}, {2}'.format(self.y, self.m, self.d))
    

    @classmethod
    def next_day(cls, today):
        return cls(today.y, today.m, today.d + 1)
        
def main():
    d1 = Date(2025, 4, 5)
    d1.show()
    d2 = Date.next_day(d1)
    d2.show()

main()
