from math import gcd


class Rational:
    def __init__(self, num=1, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise Exception("Not int")
        if den < 0:
            num, den = -num, -den
        if not den:
            raise Exception("denominator is 0")
        self.numerator = num // gcd(abs(num), abs(den))
        self.denominator = den // gcd(abs(num), abs(den))

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @numerator.setter
    def numerator(self, num):
        self.__numerator = num

    @denominator.setter
    def denominator(self, den):
        self.__denominator = den

    def __add__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator *
                        other.denominator)

    def __sub__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator *
                        other.denominator)

    def __mul__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __iadd__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        self.__init__(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator *
                      other.denominator)
        return self

    def __isub__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        self.__init__(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator *
                      other.denominator)
        return self

    def __imul__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        self.__init__(self.numerator * other.numerator, self.denominator * other.denominator)
        return self

    def __itruediv__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        self.__init__(self.numerator * other.denominator, self.denominator * other.numerator)
        return self

    def __radd__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator *
                        other.denominator)

    def __rsub__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator *
                        other.denominator)

    def __rmul__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rtruediv__(self, other):
        if not isinstance(other, (int, Rational)):
            return NotImplemented
        if isinstance(other, int):
            other = Rational(other, 1)
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __float__(self):
        return self.numerator / self.denominator

    def __lt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator * other.denominator != other.numerator * self.denominator

    def __str__(self):
        if abs(self.numerator) < self.denominator:
            return f'{self.numerator}/{self.denominator}'
        if not self.numerator % self.denominator:
            return f'{self.numerator // self.denominator}'
        if self.numerator >= 0:
            return f'{self.numerator//self.denominator} {self.numerator%self.denominator}/{self.denominator}'
        return f'-{abs(self.numerator) // self.denominator} {abs(self.numerator) % self.denominator}/{self.denominator}'


r = Rational(4, -3)
print(r)
r /= Rational(4, -3)
print(r)
print(float(r))
