import re
import json


class Note:
    def __init__(self, number, name, surname=None, age=None):
        self.name = name
        self.number = number
        self.surname = surname
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name not str")
        self.__name = name

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not isinstance(number, str):
            raise TypeError("Number not str")
        if not re.fullmatch(r'\+380\d{9}', number):
            raise TypeError("Number must follow this example!\n+380xxxxxxxxx")
        self.__number = number

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str) and surname is not None:
            raise TypeError("Surname not str")
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, name):
        if not isinstance(name, int) and name is not None:
            raise TypeError("Age not int")
        self.__age = name

    def to_dict(self):
        return {'Number': self.number, 'Name': self.name, 'Surname': self.surname, 'Age': self.age}

    def __str__(self):
        return f'Number: {self.number}, Name: {self.name}, Surname: {self.surname}, Age: {self.age}'


class Notebook:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name not str")
        self.__name = name

    def __add__(self, other):
        if not isinstance(other, Note):
            return NotImplemented
        with open(f"{self.name}.json", 'r') as f:
            k = json.load(f)
            k.append(other.to_dict())
        with open(f"{self.name}.json", 'w') as f:
            json.dump(k, f)

    def __sub__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        with open(f"{self.name}.json", 'r') as f:
            t = json.load(f)
            for record in t:
                if record['Name'] == other:
                    t.remove(record)
        with open(f"{self.name}.json", 'w') as f:
            json.dump(t, f)

    def __mul__(self, other):
        if not isinstance(other, str):
            return NotImplemented
        with open(f"{self.name}.json", 'r') as f:
            t = json.load(f)
            for record in t:
                if record['Name'] == other:
                    return str(record)
        return f'Anyone this name ' + other

    def __str__(self):
        with open(f"{self.name}.json", 'r') as f:
            t = json.load(f)
            if len(t):
                return "\n".join(map(str, t))
            return "\t\t (EMPTY)\n"


try:
    n = Notebook("NoteBook")
    n + Note("+380952263309", "Oleh", "Is_dead", 18)
    n + Note("+380952263300", "Oled")
    print(n)
    print()
    print(n * "Oleh")
    print()
    print(n)
    print()
    n - "Oleh"
    print(n)
    print()
    n - 'Oled'
    print(n * 'Oled')
except TypeError as er:
    print(er)
