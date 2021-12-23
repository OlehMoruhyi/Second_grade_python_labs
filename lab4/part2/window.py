from mysql.connector import Error
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from Classes import ITeacher, ILocalCourse, IOffsiteCourse, courseFactory


def clicked0():
    try:
        courseFactory.add_teacher(ITeacher(txt0_0.get(), txt0_1.get()))
        lbl0_0.configure(text="Успех")
    except (TypeError, Exception, Error) as er:
        lbl0_0.configure(text=er)


def clicked1():
    try:
        if combo1_0.get() == "Локальный":
            courseFactory.add_local(ILocalCourse(txt1_0.get(), txt1_1.get(), int(txt1_2.get()), txt1_3.get()))
            lbl1_0.configure(text="Успех))")
        elif combo1_0.get() == "Выездной":
            courseFactory.add_offsite(IOffsiteCourse(txt1_0.get(), txt1_1.get(), int(txt1_2.get()), txt1_3.get()))
            lbl1_0.configure(text="Успех))")
        else:
            lbl1_0.configure(text=combo1_0.get() + " не тип курса, что вы вообще ввели?")
    except (TypeError, Exception, Error) as er:
        lbl1_0.configure(text=er)


def clicked2_0():
    txt2_1.delete(1.0, END)
    try:
        txt2_1.insert(END, courseFactory.teachers())
        lbl2_0.configure(text="Успех))")
    except (TypeError, Exception, Error) as er:
        lbl2_0.configure(text=er)


def clicked2_1():
    txt2_1.delete(1.0, END)
    try:
        txt2_1.insert(END, courseFactory.courses())
        lbl2_0.configure(text="Успех))")
    except (TypeError, Exception, Error) as er:
        lbl2_0.configure(text=er)


def clicked2_2():
    txt2_1.delete(1.0, END)
    try:
        txt2_1.insert(END, courseFactory.one_teacher(int(txt2_0.get())))
        lbl2_0.configure(text="Успех))")
    except (TypeError, Exception, Error) as er:
        lbl2_0.configure(text=er)


window = Tk()
window.title("Курсы")
window.geometry('1000x700')


tab_control = ttk.Notebook(window)
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)


tab_control.add(tab0, text='Новый преподаватель')
tab_control.add(tab1, text='Новый курс')
tab_control.add(tab2, text='Запросы')


Label(tab0, text='Имя').grid(column=0, row=0)
txt0_0 = Entry(tab0, width=50)
txt0_0.grid(column=1, row=0)
Label(tab0, text='Фамилия').grid(column=0, row=1)
txt0_1 = Entry(tab0, width=50)
txt0_1.grid(column=1, row=1)
lbl0_0 = Label(tab0, text="Удачи")
lbl0_0.grid(column=1, row=10)
btn0_0 = Button(tab0, text="Нажимать!", command=clicked0)
btn0_0.grid(column=0, row=10)


Label(tab1, text='Название').grid(column=0, row=0)
txt1_0 = Entry(tab1, width=50)
txt1_0.grid(column=1, row=0)
Label(tab1, text='Программа').grid(column=0, row=1)
txt1_1 = Entry(tab1, width=50)
txt1_1.grid(column=1, row=1)
Label(tab1, text='ID преподавателя').grid(column=0, row=2)
txt1_2 = Entry(tab1, width=50)
txt1_2.grid(column=1, row=2)
Label(tab1, text='Тип курса').grid(column=0, row=3)
combo1_0 = Combobox(tab1)
combo1_0['values'] = ("Локальный", "Выездной")
combo1_0.current(0)  # установите вариант по умолчанию
combo1_0.grid(column=1, row=3)
Label(tab1, text='Лаборатория/город').grid(column=0, row=4)
txt1_3 = Entry(tab1, width=50)
txt1_3.grid(column=1, row=4)
lbl1_0 = Label(tab1, text="Удачи")
lbl1_0.grid(column=1, row=10)
btn1_0 = Button(tab1, text="Нажимать!", command=clicked1)
btn1_0.grid(column=0, row=10)


frame = Frame(tab2, relief=RAISED, bd=2)
btn2_0 = Button(frame, text='Все преподаватели', width=20, command=clicked2_0)
btn2_0.grid(column=0, row=0)
btn2_1 = Button(frame, text='Все курсы', width=20, command=clicked2_1)
btn2_1.grid(column=0, row=1)
btn2_2 = Button(frame, text='Все курсы преподавателя', width=20, command=clicked2_2)
btn2_2.grid(column=0, row=2)
txt2_0 = Entry(frame, width=10)
txt2_0.grid(column=0, row=3)
frame.grid(column=0, row=0)
lbl2_0 = Label(tab2, text="Удачи")
lbl2_0.grid(column=0, row=10)
txt2_1 = scrolledtext.ScrolledText(tab2, width=100, height=30)
txt2_1.grid(column=1, row=0)


tab_control.pack(expand=1, fill='both')
window.mainloop()
