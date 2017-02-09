import math

decades, sum = [], 0
for n in range(1, 10):
    sum += n * 9 * (10 ** (n - 1))
    decades.append(sum)

for k in range(int(input())):
    n = int(input())

    if n < 9:
        print(n)
        continue

    decade = 0
    for i in range(10):
        if n > decades[i]:
            decade += 1
        else:
            break

    print(str(10 ** decade + math.ceil((n - decades[decade - 1]) / (decade + 1)) - 1)[
              ((n - decades[decade - 1]) % (decade + 1)) - 1])
