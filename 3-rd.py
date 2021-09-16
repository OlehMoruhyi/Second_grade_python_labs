from sys import argv

# checklist for numbers and expression symbols
num_list = '1234567890'
exp_list = '-+*/%'


def assay(t):
    ind = 1
    for q in t:
        if q in num_list:
            ind = 1
        elif q in exp_list:
            if ind:
                ind = 0
            else:
                return False
        elif ind != 10 and (q == '(' or ')'):
            ind = 10
        else:
            return False
    return ind


exp = ''.join(argv[1:])
if assay(exp):
    print('(True, {})' .format(eval(exp)))
else:
    print('(False, None)')
