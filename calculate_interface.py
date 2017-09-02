# -*- coding: utf-8 -*-

"""
Написать программу которая бы выводила результат операции сложения двух значений

Описание программы:
Окно с 3-мя полями, два из которых являются полями ввода, и одно поле отображает результат.
Также в интерфейсе программы присутствует кнопка которая запускает просчет и отображение результата

Ссылка на описание библиотеки Tkinter:
"""
#https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python

from Tkinter import *


# функция сложения двух значений
def add(x, y):
    return x+y


# функция очистки и вставки результата
def clear_insert(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)


# функция обработки событий
def handler():
        first_arg = int(a.get())
        second_arg = int(b.get())
        clear_insert(add(first_arg, second_arg))

root = Tk()
root.title('Addition calculator')
root.minsize(325, 230)
root.resizable(width=False, height=False)
frame = Frame(root)
frame.grid()

# поле ввода первого аргумента
a = Entry(frame, bg='lightblue', width=3)
a.grid(row=5, column=1, padx=(10, 0))
# текст после первого аргумента
a_lab = Label(frame, text="+").grid(row=5, column=2)

# поле ввода второго аргумента
b = Entry(frame, bg='lightblue', width=3)
b.grid(row=5, column=3)
# текст после второго аргумента
b_lab = Label(frame, text="=").grid(row=5, column=4)

# кнопка подсчитать
but = Button(frame, text="Calculate", command=handler).grid(row=5, column=7, padx=(10, 0))

# место вывода результата
output = Text(frame, bg="lightblue", font="Arial 10", width=5, height=1)
output.grid(row=5, column=6)

# запуск окна
root.mainloop()
