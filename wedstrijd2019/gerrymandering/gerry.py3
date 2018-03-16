best = (0, 0, 0)


def gerry(rooster, s, b, l):
    if rooster == [[]]:
        return

    if len(rooster) != 1:
        boven_weg = rooster[1:]
        onder_weg = rooster[:-1]

        gerry2(boven_weg, s, rooster[0], True, False)
        if not b:
            gerry2(onder_weg, s, rooster[-1], False, False)
    if len(rooster[0]) != 1:
        links_weg = [lijn[1:] for lijn in rooster]
        rechts_weg = [lijn[:-1] for lijn in rooster]

        gerry2(links_weg, s, [lijn[0] for lijn in rooster], False, True)
        if not l:
            gerry2(rechts_weg, s, [lijn[-1] for lijn in rooster], False, False)

    gerry2([[]], s, [i for lijn in rooster for i in lijn], False, False)


def gerry2(rooster, s, m, boven, links):
    global best
    a = sum(m)
    b = len(m) - a

    blabla = False
    if a > b:
        s = (s[0] + 1, s[1], s[2])
    elif a == b:
        s = (s[0], s[1] + 1, s[2])
    elif a < b:
        if s == best:
          blabla = True
        s = (s[0], s[1], s[2] - 1)
    if not blabla:
        best = max(best, s)
    else:
        best = s
    gerry(rooster, s, boven, links)


for ni in range(int(input())):
    tekens, aantallijnen = list(map(int, input().split(" ")))

    matrix = []

    for li in range(aantallijnen):
        lijn = list(map(lambda char: char == 'A', (c for c in str(input()))))
        matrix.append(lijn)

    best = (0, 0, 0)

    gerry(matrix, best, False, False)

    best = (best[0], best[1], 0-best[2])

    print("{} {}".format(ni + 1, " ".join(map(str, best))))
