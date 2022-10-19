def adder(f1, f2):
    return f1 + f2


def identity(n):
    return n


def square(n):
    return n**2


def a1(num):
    return adder(identity(num), square(num))


print(a1(4))
a2 = adder(a1(4), identity(4))
print(a2)
a2 = adder(a1(5), identity(5))
print(a2)
a3 = adder(a1(4), identity(4))
print(a3 + a1(4))
