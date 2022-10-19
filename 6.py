def smth(g, dx):
    return lambda x: (g(x - dx) + g(x) + g(x + dx)) / 3


square = lambda x: x ** 2
smoothed = smth(square, 1)
print(round(smth(square, 1)(0), 3))
