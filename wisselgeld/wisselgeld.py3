def count(n, ms):
    table = [0 for k in range(n+1)]
    table[0] = 1

    for i in range(0, len(ms)):
        for j in range(ms[i], n+1):
            table[j] += table[j-ms[i]]

    return table[n]


for s in range(int(input())):
    line = str(input()).split(' ', 1)
    n = int(line[0])
    ms = [int(i) for i in line[1].split(' ')]
    print(count(n, ms))
