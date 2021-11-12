import timeit


def itg1():
    summ = 0
    with open("test.txt", "r") as f:
        for x in f.readlines():
            x.strip().isdigit()
            if True:
                summ += int(x.strip())
    return summ


def itg2():
    summ = 0
    with open("test.txt", "r") as f:
        for x in f:
            x.strip().isdigit()
            if True:
                summ += int(x.strip())
    return summ


def itg3():
    with open("test.txt", "r") as f:
        x = (int(i.strip()) for i in f if i.strip().isdigit())
        return sum(x)


print(timeit.timeit(itg1, number=10))
print(timeit.timeit(itg2, number=10))
print(timeit.timeit(itg3, number=10))
