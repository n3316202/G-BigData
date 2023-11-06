# point_3dict.py

class Point3D:
    def __init__(self, x, y, z):
        self.x = x       # x 좌표
        self.y = y       # y 좌표
        self.z = z       # z 좌표
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)


def main():
    p = Point3D(24, 17, 31)       # 3차원 좌표상의 한 점
    print(p.x, p.y, p.z)
    print(p.__dict__['x'], p.__dict__['y'], p.__dict__['z'])

main()
