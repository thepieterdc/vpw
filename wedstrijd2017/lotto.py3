n = int(input())
for k in range(n):
    w = [0, 0, 0, 5, 22, 1201, 1000000]
    wb = [0, 0, 3, 8, 218, 35722]

    juiste = str(input()).split(' ')
    bonus = int(juiste[-1])
    get = list(map(int, juiste[:-1]))
    i = int(input())
    winst = 0
    for _ in range(i):
        aantal = 0
        b = False
        gok = map(int, str(input()).split(' '))
        for g in gok:
            if g in get:
                aantal += 1
            else:
                if g == bonus:
                    b = True
        if b:
            winst += wb[aantal]
        else:
            winst += w[aantal]

    print("{} {}".format(k + 1, winst))
