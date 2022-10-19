def increment(num):
    return num + 1


def identity(num):
    return 1 * num


def square(num):
    return num * num


def triple(num):
    return 3 * num


def intscts(f, x):
    def func(g):
        if f(x) == g(x):
            return True
        return False

    return func


at_three = intscts(square, 3)
print(at_three(triple))
print(at_three(increment))
at_one = intscts(identity, 1)
print(at_one(square))
print(at_one(triple))
