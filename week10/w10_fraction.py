class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        self.a = a
        self.b = b

    def show(self):
        a = abs(self.a)
        b = abs(self.b)
        if self.a * self.b < 0:
            print(f'-{a}/{b}', end='')
        else:
            print(f'{a}/{b}', end='')
    