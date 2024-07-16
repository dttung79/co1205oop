from w8_circle import Circle
from w8_rectangle import Rectangle, Square

def run():
    r = Rectangle('EFGH', 5, 10)
    s = Square('ABCD', 10)
    c = Circle('O', 5)

    shapes = [r, s, c]

    for s in shapes:
        print(s)

if __name__ == '__main__':
    run()