def add_one(x):
    return x + 1


def times_two(x):
    return x * 2


def add_three(x):
    return x + 3


def cyc(g1, g2, g3):
    def func(n):
        def inner_func(x):
            nonlocal n
            if n == 0:
                return x
            elif n == 1:
                return g1(x)
            elif n == 2:
                return g2(g1(x))
            else:
                n -= 3
                return inner_func(g3(g2(g1(x))))
        return inner_func
    return func


my_cyc = cyc(add_one, times_two, add_three)
h = my_cyc(0)
print(h(5))

h = my_cyc(2)
print(h(1))

h = my_cyc(3)
print(h(2))

h = my_cyc(4)
print(h(2))

h = my_cyc(6)
print(h(1))
