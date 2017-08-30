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


int_argv1 = int(sys.argv[2])
int_argv2 = int(sys.argv[3])

if (0 <= int_argv1 <= 10) and (0 <= int_argv2 <= 10):
    if sys.argv[1] == '-add':
        print int_argv1 + int_argv2
    elif sys.argv[1] == '-mul':
        print int_argv1 * int_argv2
    elif sys.argv[1] == '-sub':
        print int_argv1 - int_argv2
    elif sys.argv[1] == '-div':
        if int_argv2 != 0:
            print int_argv1 / int_argv2
        else:
            print 'Division by zero.\nEnter the value of the second argument from 1 to 10.'
    else:
        print 'Invalid function name.\nPossible Functions: -add, -mul, -sub, -div.'
else:
    print 'Invalid parameter value(s).\nPossible parameter value(s) from 0 to 10.'


