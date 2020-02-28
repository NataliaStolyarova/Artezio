"""Arithmetic operations with complex numbers."""


class ComplexNumbers:
    """Class describing complex numbers
    and realises arithmetic operations."""

    def __init__(self, inp_str):
        self.real = float(inp_str[0])
        self.imag = float(inp_str[1])

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumbers([real, imag])

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumbers([real, imag])

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumbers([real, imag])

    def __truediv__(self, other):
        real = (self.real * other.real + self.imag * other.imag) /\
               (other.real ** 2 + other.imag ** 2)
        imag = (self.imag * other.real - self.real * other.imag) /\
               (other.real ** 2 + other.imag ** 2)
        return ComplexNumbers([real, imag])

    def __abs__(self):
        real = (self.real ** 2 + self.imag ** 2)**0.5
        return ComplexNumbers([real, 0])

    def __repr__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format("%.2f" % self.real, sign, "%.2f" % self.imag)


if __name__ == "__main__":
    C = ComplexNumbers(input("Enter x: ").split())
    D = ComplexNumbers(input("Enter y: ").split())
    print(C + D)
    print(C - D)
    print(C * D)
    print(C / D)
    print(abs(C))
    print(abs(D))
