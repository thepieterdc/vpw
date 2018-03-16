def uniek_landen(hoogte, breedte, letters):
    posities = [(x, y) for x in range(hoogte) for y in range(breedte)]
    i = 0

    while posities:
        x, y = posities[0]
        del posities[0]
        letter = letters[x][y]
        eiland = [(x, y)]
        while eiland:
            x, y = eiland[0]
            del eiland[0]
            if x != 0:
                l = letters[x - 1][y]
                if l == letter:
                    eiland.append((x - 1, y))
            elif y != 0:
                l = letters[x][y - 1]
                if l == letter:
                    eiland.append((x, y - 1))
            elif x < hoogte:
                l = letters[x + 1][y]
                if l == letter:
                    eiland.append((x + 1, y))
            elif y < breedte:
                l = letters[x][y + 1]
                if l == letter:
                    eiland.append((x, y + 1))
            letters[x][y] = i
            if (x - 1, y) in posities:
                posities.remove((x - 1, y))
        i += 1
    return letters


for case in range(int(input())):
    b, h = (int(i) for i in input().split(" "))

    grid = []

    for hi in range(h):
        hoogtes = list(input())
        grid.append(hoogtes)

    print(uniek_landen(h, b, grid))
