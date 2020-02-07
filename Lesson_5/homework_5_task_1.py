"""Arithmetic operations with complex numbers"""


class ComplexNumbers:
    """Class describing complex numbers"""
    def __init__(self, real=None, imag=None):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format("%.2f" % self.real, sign, "%.2f" % self.imag)

    __repr__ = __str__

    def __round__(self, positions):
        print(ComplexNumbers(round(self.real, 2), round(self.imag, 2)))


class Operations:
    """Class that realises arithmetic operations"""
    def __add__(self, a, b):
        real = a.real + b.real
        imag = a.imag + b.imag
        print(ComplexNumbers(real, imag))

    def __sub__(self, a, b):
        real = a.real - b.real
        imag = a.imag - b.imag
        print(ComplexNumbers(real, imag))

    def __mul__(self, a, b):
        real = a.real * b.real - a.imag * b.imag
        imag = a.imag * b.real + a.real * b.imag
        print(ComplexNumbers(real, imag))

    def __divmod__(self, a, b):
        real = (a.real * b.real + a.imag * b.imag) / \
               (b.real ** 2 + b.imag ** 2)
        imag = (a.imag * b.real - a.real * b.imag) / \
               (b.real ** 2 + b.imag ** 2)
        print(ComplexNumbers(real, imag))

    def mod_of_num(self, a):
        mod = (a.real ** 2 + a.imag ** 2) ** 0.5
        print(mod)


x = ComplexNumbers(2, 1)
y = ComplexNumbers(5, 6)

op = Operations()
op.__add__(x, y)
op.__sub__(x, y)
op.__mul__(x, y)
op.__divmod__(x, y)
op.mod_of_num(x)
op.mod_of_num(y)
