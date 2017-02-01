from math import ceil, sqrt

for k in range(int(input())):
    x, y = input().split(' ')
    x, y = int(x), int(y)
    ret = -1
    while x < y:
        s = sum({n + (x // n if (n ** n != x) else 0) for n in range(1, ceil(sqrt(x)) + 1) if x % n == 0})
        if s % x == 0:
            ret = s // x
            break
        x += 1

    print("GEEN" if ret == -1 else "{} {}".format(x, ret))
