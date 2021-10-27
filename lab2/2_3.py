class Student:
    def __init__(self, surname, name, patronymic, number):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(patronymic, str) \
                or not isinstance(number, int):
            raise Exception
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__number = number
        self.__grades = {}

    def __str__(self):
        return f'Surname: {self.surname}, name: {self.name}, patronymic: {self.patronymic}, number: {self.number}, ' \
               f'Avarage grade: {self.avarage_grade()};'

    def avarage_grade(self):
        if len(self.__grades) == 0:
            return 0
        avarage = 0
        for i in self.__grades.values():
            avarage += sum(i) / len(i)
        return avarage / len(self.__grades)

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def number(self):
        return self.__number

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, dict):
            raise Exception
        self.__grades = grades

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise Exception
        self.__surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception
        self.__name = name

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise Exception
        self.__patronymic = patronymic

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise Exception
        self.__number = number

    def add_grade(self, name, grade):
        if not isinstance(name, str) or not isinstance(grade, int):
            raise Exception
        if grade < 0 or grade > 100:
            raise Exception
        if not self.__grades.get(name):
            self.__grades.update({name: [grade]})
        else:
            new = self.__grades.get(name) + [grade]
            self.__grades.update({name: new})

    def show_grades(self):
        kk = '\n\t'
        return f'Grades:\n\t{kk.join(map(str, self.__grades.items()))}'


class Group:
    def __init__(self, name, students=[]):
        self.number = 0
        self.__name = name
        self.__students = []
        self.add_student(students)

    @property
    def name(self):
        return self.__name

    @property
    def students(self):
        return self.__students

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception
        self.__name = name

    @students.setter
    def students(self, students):
        if not isinstance(students, list) or not all(isinstance(x, Student) for x in students):
            raise Exception
        self.__students = students

    def __str__(self):
        kk = "\n\t"
        return f'Name: {self.name}\nCount: {self.number}\nGroup:\n\t' \
               f'{kk.join(map(str, sorted(self.__students, key=lambda x: x.avarage_grade(), reverse=True)[:5]))}'

    def add_student(self, students):
        if not isinstance(students, list) or not all(isinstance(x, Student) for x in students) and self.number >= 20:
            raise Exception
        for i in students:
            for k in self.students:
                if (i.surname, i.name) == (k.surname, k.name):
                    raise Exception
            self.students += [i]
        self.number += len(students)

    def del_student(self, num):
        if isinstance(num, int) and 0 < num <= self.number:
            self.__students.pop(num-1)
            self.number -= 1
        else:
            raise Exception


try:
    student = Student('a', 's', 'd', 1)
    group = Group('17', [Student('l', 'sd', 'ds', 4), Student('b', 'l', 'd', 3)])
    group.add_student([student, Student('a', 'd', 'd', 3), Student('a', 'sd', 'ds', 4)])
    group.add_student([Student('b', 'sd', 'ds', 4), Student('b', 'd', 'd', 3), Student('ab', 'sd', 'ds', 4)])
    student.add_grade('Math', 1)
    student.add_grade('Math', 2)
    student.add_grade('Mat', 1)
    group.students[1].add_grade('Math', 1)
    print(group)
except(Exception, TypeError):
    print('Error!')
