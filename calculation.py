# -*- coding: utf-8 -*-

"""Написать программу которая работает с коммандной строкой

Программа принимает 3 аргумента в коммандной строке.
Первый аргумент это одна из математических функций, а именно:
-add - математическое сложение
-mul - математическое умножение
-sub - математическое вычитание
-div - математическое деление

Запуск программы:
python <program_name> -func -parameter1 -parameter2

Где опции могут быть:
-func - математическая функция, принимает значение -add, -mul, -sub, -div
-parameter1 - первый параметр, принимает значени от 0 до 10
-parameter2 - первый параметр, принимает значени от 0 до 10

Программа возвращает единственное значение в формате int посчитанное согласно введенного параметра -func"""

import sys


def add(x, y):
    return x+y


def mul(x, y):
    return x*y


def sub(x, y):
    return x-y


def div(x, y):
    return x/y


def command_line(first_arg, second_arg, third_arg):
    second_arg = int(second_arg)
    third_arg = int(third_arg)

    if (0 <= second_arg <= 10) and (0 <= third_arg <= 10):
        if first_arg == '-add':
            return add(second_arg, third_arg)
        elif first_arg == '-mul':
            return mul(second_arg, third_arg)
        elif first_arg == '-sub':
            return sub(second_arg, third_arg)
        elif first_arg == '-div':
            if third_arg != 0:
                return div(second_arg, third_arg)
            else:
             return 'Division by zero.\nEnter the value of the second argument from 1 to 10.'
        else:
            return 'Invalid function name.\nPossible Functions: -add, -mul, -sub, -div.'
    else:
        return 'Invalid parameter value(s).\nPossible parameter value(s) from 0 to 10.'

print command_line(sys.argv[1], sys.argv[2], sys.argv[3])
