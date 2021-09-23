from sys import argv
from operator import add, pow, mul, sub, truediv

num_list = '1234567890'
exp_list = ['add', 'pow', 'mul', 'sub', 'truediv']


def assay():
    if len(argv) != 4:
        return False
    if (argv[1] in exp_list) is False:
        return False
    if (argv[2] in num_list) is False:
        return False
    if (argv[3] in num_list) is False:
        return False
    return True


if assay():
    print(eval(argv[1] + '(' + argv[2] + ', ' + argv[3] + ')'))
else:
    print('Incorrect expression')
