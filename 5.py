def f(n):
    # print(f"f()()({n})()")
    return f"f()()({n})()\n{n}"


print(f(3))


def f():
    def f():
        def f(n):
            def f():
                return n
            return f
        return f
    return f


x = f()()(3)()
print(x)
