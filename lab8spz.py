# -*- coding: utf-8 -*-
import random
import numexpr


def expression_generate():
    first_random = random.randint(3, 3)
    expression = []
    arithmetic_signs = ['+', '-', '*', '/']
    while first_random != 0:
        random_number = float(random.randrange(1, 10))
        if len(expression) % 2 == 0:
            expression.append(str(random_number))
        else:
            break
        random_arithmetic_sign = random.choice(arithmetic_signs)
        if len(expression) % 2 == 1:
            expression.append(random_arithmetic_sign)
        else:
            break
        first_random -= 1
    expression.pop()
    expression.insert(0, '(')
    expression.append(')')
    return ''.join(expression)


def final_expression_gen():
    second_random = random.randint(2, 5)
    final_expression = []
    arithmetic_signs = ['+', '-', '*', '/']
    while second_random != 0:
        final_expression.append(''.join(expression_generate()))
        if len(final_expression) % 2 == 1:
            final_expression.append(random.choice(arithmetic_signs))
        else:
            break
        second_random -= 1
    final_expression.pop()
    return final_expression


final = final_expression_gen()
print 'Infix form: ', ''.join(final)


def calc(final_expr):
    exprs = []
    for item in final_expr:
        if item not in ['+', '-', '*', '/']:
            exprs.append(str(round(float(numexpr.evaluate(item)), 2)))
        else:
            exprs.append(item)
    return exprs


print 'Result of Infix form: ', round(numexpr.evaluate(''.join(calc(final))), 2)


AllowedOperators = { #словарь(ассоциативный массив) операторов
    '-':float.__sub__, #определяем ключи к операторам,и действия которые они выполняют
    '+':float.__add__,
    '*':float.__mul__,
    '/':float.__div__,
}

Priority = {#словарь приоритетов операторов
    '*':3,
    '/':3,
    '+':2,
    '-':2,
    '(':1,
}


def allowed_nums(): #возвращает разрешимые ЦИФРЫ
    return '0123456789.'


def return_polish_record(expression):
    issearch = False
    stack = []
    outstring = ''
    iter = 0
    for symbol in expression:
        if symbol == '-':
            try:
                if expression[iter+1] in allowed_nums():
                    outstring += symbol
                    iter += 1
                    continue
            except IndexError:
                pass
        if symbol == ')':
            i = 0
            for elem in stack:
                if elem == '(':
                    pos = i
                i += 1
            if pos < len(stack):
                stack.pop(pos)
            k=len(stack)
            while k > pos:
                outstring += stack.pop()
                k -= 1
            outstring += ') '
        if symbol in allowed_nums():
            try:
                if expression[iter+1] in allowed_nums():
                    outstring += symbol
                else:
                    outstring += symbol+' '
            except IndexError:
                outstring += symbol+' '
        if symbol == '(':
            stack.append(symbol)
            outstring += ' ('
        if symbol in AllowedOperators.keys():
            if not stack:
                stack.append(symbol)
            else:
                if Priority[symbol] > Priority[stack[-1]]:
                    stack.append(symbol)
                else:
                    cnt = 0
                    for elem in stack:
                        if elem == '(':
                            while cnt < len(stack):
                                if Priority[stack[cnt]] >= Priority[symbol]:
                                    outstring += stack.pop(cnt)+' '
                                cnt += 1
                            stack.append(symbol)
                            issearch = True
                            break
                        cnt += 1
                        if not issearch:
                            for elem in stack:
                                if Priority[elem] >= Priority[symbol]:
                                    i = 0
                                    while stack[i] != elem:
                                        i += 1
                                    outstring += stack.pop(i)+' '
                            stack.append(symbol)
        iter += 1
    for elem in reversed(stack):
        outstring += elem+' '
    return outstring


print 'Postfix form: ', return_polish_record(''.join(final))
print 'Result of Postfix form: ', round(numexpr.evaluate(''.join(calc(final))), 2)



