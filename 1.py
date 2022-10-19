def abndnt(n):
    num = []
    for i in range(1, n):
        if n % i == 0:
            print(f"{i} * {n // i}")
            num.append(i)
    #     else:
    #         print("Buzz")
    # print(num)

    total = 0
    for j in num:
        total += j
    if total > n:
        print("True\n")
    else:
        print("False\n")


abndnt(12)
abndnt(14)
abndnt(16)
abndnt(20)
abndnt(22)
abndnt(24)
