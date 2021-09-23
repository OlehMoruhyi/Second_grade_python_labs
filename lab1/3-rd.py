from sys import argv

# checklist for numbers and expression symbols
num_list = '1234567890'
exp_list = '-+*/%'


def assay(t):
    ind = 0
    for q in t:
        if q in num_list:
            ind = 1
        elif (q in exp_list) and (ind != 0):
            ind = 0
        elif (q == '(' or q == ')') and ind != 10:
            ind = 10
        else:
            return False
    return ind


exp = ''.join(argv[1:])
if assay(exp):
    print('(True, {})' .format(eval(exp)))
else:
    print('(False, None)')
