import sys
# from math import functions
from math import cos, acos, cosh, acosh, sin, asin, sinh, asinh, tan, atan, tanh, atanh, fabs, pow, sqrt


# add functions of + - * /
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# checklist for correct input function
exp_list = ['cos', 'acos', 'cosh', 'acosh', 'sin', 'asin', 'sinh', 'asinh', 'tan', 'atan', 'tanh', 'atanh', 'fabs',
            'pow', 'sqrt', 'plus', 'minus', 'multiply', 'devide']
if sys.argv[1] in exp_list:
    result = 0
    exp = 'result = ' + sys.argv[1] + '(' + sys.argv[2]
    if sys.argv[4]:
        exp += ', ' + sys.argv[4]
    exp += ')'
    exec(exp)
    print(result)
else:
    print('unknown expression')
