class Rectangle:
    def __init__(self):
        self.__length = 1
        self.__width = 1

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        try:
            self.__length = float(length)
            if not 0.0 < self.__length < 20.0:
                raise ValueError

        except ValueError:
            print('An error in entered data. Length = 1.0')

    @width.setter
    def width(self, width):
        try:
            self.__width = float(width)
            if not 0.0 < self.__width < 20.0:
                raise ValueError

        except ValueError:
            print('An error in entered data. Width = 1.0')


    def perimeter_getter(self):
        return (self.__length + self.__width) * 2

    def square_getter(self):
        return self.__length * self.__width


r1 = Rectangle()
r1.length = 2.4
r1.width = input()
print(r1.perimeter_getter())
