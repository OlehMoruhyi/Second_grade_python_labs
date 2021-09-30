class Rational:
    numerator = 1
    denominator = 1

    def __init__(self, n=1, d=1):
        try:
            n, d = int(n), int(d)
            self.numerator = int(n / gcd(n, d))
            self.denominator = int(d / gcd(n, d))

        except ValueError:
            print('ValueError')

    def out(self):
        print(self.numerator, '/', self.denominator, sep='')

    def float_out(self):
        print(self.numerator / self.denominator)


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


r = Rational(input('Enter numerator: '), input('Enter denominator: '))
r.out()
r.float_out()
