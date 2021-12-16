from MySqlConnector import connection as con
from MySqlConnector import teacherID, coursesID


class ITeacher:
    counter = teacherID

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        ITeacher.counter += 1
        self.id_teacher = ITeacher.counter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or name == '':
            raise TypeError("Name non string(((")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str) or surname == '':
            raise TypeError("Surname non string(((")
        self.__surname = surname

    @property
    def id_teacher(self):
        return self.__id_teacher

    @id_teacher.setter
    def id_teacher(self, id_teacher):
        self.__id_teacher = id_teacher

    def to_array(self):
        return self.id_teacher, self.name, self.surname


class ICourse:
    counter = coursesID

    def __init__(self, name, program, teacher):
        self.name = name
        self.program = program
        self.teacher = teacher
        ICourse.counter += 1
        self.id_course = ICourse.counter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or name == '':
            raise TypeError("Name non string(((")
        self.__name = name

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, program):
        if not isinstance(program, str) or program == '':
            raise TypeError("Program non string(((")
        self.__program = program

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, int):
            raise TypeError("Teacher id non int(((")
        if teacher > ITeacher.counter:
            raise Exception("Unknown teacher id(((")
        self.__teacher = teacher

    @property
    def id_course(self):
        return self.__id_course

    @id_course.setter
    def id_course(self, id_course):
        if not isinstance(id_course, int):
            raise TypeError("I don`t know how you do this(((")
        self.__id_course = id_course


class ILocalCourse(ICourse):
    def __init__(self, name, program, teacher, lab):
        super().__init__(name, program, teacher)
        self.lab = lab

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, lab):
        if not isinstance(lab, str) or lab == '':
            raise TypeError("Lab not str((")
        self.__lab = lab

    def to_array(self):
        return self.id_course, self.name, self.program, self.teacher, self.lab


class IOffsiteCourse(ICourse):
    def __init__(self, name, program, teacher, city):
        super().__init__(name, program, teacher)
        self.city = city

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if not isinstance(city, str) or city == '':
            raise TypeError("City not str((")
        self.__city = city

    def to_array(self):
        return self.id_course, self.name, self.program, self.teacher, self.city


class CourseFactory:
    def __init__(self, connection):
        self.connection = connection

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    def add_teacher(self, teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError("Teacher not teacher, funny)))")
        insert = f'INSERT INTO teacher(id, Name1, Surname) value {str(teacher.to_array())}'
        print(insert)
        self.connection.cursor().execute(insert)
        self.connection.commit()

    def add_teacher(self, teacher):
        if not isinstance(teacher, ITeacher):
            raise TypeError("Teacher not teacher, funny)))")
        insert = f'INSERT INTO teacher(id, Name1, Surname) value {str(teacher.to_array())}'
        self.connection.cursor().execute(insert)
        self.connection.commit()

    def add_local(self, local):
        if not isinstance(local, ILocalCourse):
            raise TypeError("Local course not local, sorry((")
        insert = f'INSERT INTO LocalCourses(id, Name1, Program, Teacher, lab) value {str(local.to_array())}'
        print(insert)
        self.connection.cursor().execute(insert)
        self.connection.commit()

    def add_offsite(self, local):
        if not isinstance(local, IOffsiteCourse):
            raise TypeError("Offsite course not offsite, sorry((")
        insert = f'INSERT INTO OffsiteCourses(id, Name1, Program, Teacher, city) value {str(local.to_array())}'
        print(insert)
        self.connection.cursor().execute(insert)
        self.connection.commit()

    def teachers(self):
        select = "SELECT * FROM Teacher"
        f = ''
        with self.connection.cursor() as cursor:
            cursor.execute(select)
            for r in cursor.fetchall():
                f += f'Id - {r[0]}; Name - {r[1]}; Surname - {r[2]};\n'
        return f

    def one_teacher(self, teacher_id):
        if not isinstance(teacher_id, int):
            raise TypeError("Strange id")
        select = f'SELECT id, Name1, Program, Teacher, lab as place FROM LocalCourses where Teacher = {teacher_id} ' \
                 f'UNION SELECT id, Name1, Program, Teacher, city as place FROM OffsiteCourses where Teacher = {teacher_id} ' \
                 f'order by id'
        f = ''
        with self.connection.cursor() as cursor:
            cursor.execute(select)
            for r in cursor.fetchall():
                f += f'Id - {r[0]}; Name - {r[1]}; Program - {r[2]}; Teacher id - {r[3]}; Place - {r[4]};\n'
        return f

    def courses(self):
        select = f'SELECT id, Name1, Program, Teacher, lab as place FROM LocalCourses ' \
                 f'UNION SELECT id, Name1, Program, Teacher, city as place FROM OffsiteCourses ' \
                 f'order by id'
        f = ''
        with self.connection.cursor() as cursor:
            cursor.execute(select)
            for r in cursor.fetchall():
                f += f'Id - {r[0]}; Name - {r[1]}; Program - {r[2]}; Teacher id - {r[3]}; Place - {r[4]};\n'
        return f


ICourseFactory = CourseFactory(con)
