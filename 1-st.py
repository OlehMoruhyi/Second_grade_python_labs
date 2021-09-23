from sys import argv


# checklist for numbers and expression symbols
num_list = '1234567890'
exp_list = '-+*/'


def assay():
    if len(argv) != 4:
        return False
    if (argv[1] in num_list) is False:
        return False
    if (argv[2] in exp_list) is False or (argv[2] == '/' and argv[3] == '0'):
        return False
    if (argv[3] in num_list) is False:
        return False
    return True


if assay():
    print(eval(' '.join(argv[1:])))
else:
    print('Incorrect expression')
