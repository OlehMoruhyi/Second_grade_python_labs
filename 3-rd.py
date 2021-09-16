import sys

# checklist for numbers and expression symbols
num_list = '1234567890'
exp_list = '-+*/%'


def assay(t):
    ind = 1
    for q in t:
        if q in num_list:
            ind = 1
        elif ind and q in exp_list:
            ind = 0
        elif ind == 1 and (q == '(' or ')'):
            ind = 10
        else:
            return False
    return ind


exp = ''
for i in range(1, len(sys.argv)):
    exp += sys.argv[i]
if assay(exp):
    print('(True, {})' .format(eval(exp)))
else:
    print('(False, None)')
