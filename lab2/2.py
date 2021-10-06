class Rational:
    def __init__(self, n=1, d=1):
        try:
            n, d = int(n), int(d)
            if d == 0:
                raise ValueError
            if d < 0:
                n, d = -n, -d
            self.__numerator = int(n / gcd(abs(n), abs(d)))
            self.__denominator = int(d / gcd(abs(n), abs(d)))
        except ValueError:
            self.__numerator = 1
            self.__denominator = 1
            print('An error in entered data. Numerator = 1, denominator = 1')

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
    def denominator(self, num):
        self.__denominator = num

    def out(self):
        return f'{self.numerator} / {self.denominator}'

    def float_out(self):
        return self.numerator / self.denominator


def gcd(a, b):
    if not a or not b:
        return 1
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


r = Rational(input('Enter numerator: '), input('Enter denominator: '))
print(r.out())
print(r.float_out())
