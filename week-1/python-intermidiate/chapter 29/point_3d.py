# point_3d.py

class Point3D:
    def __init__(self, x, y, z):
        self.x = x       # x 좌표
        self.y = y       # y 좌표
        self.z = z       # z 좌표
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x, self.y, self.z)


def main():
    p1 = Point3D(1, 1, 1)      # 3차원 좌표상의 한 점
    p2 = Point3D(24, 17, 31)       # 3차원 좌표상의 한 점
    print(p1)
    print(p2)

main()
