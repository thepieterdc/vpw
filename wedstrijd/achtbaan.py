def stap(richting, loc, kubus, stap):
    h, z, o = loc
    nrichting = richting
    if richting == "N":
        if stap == "S":
            kubus[h][z][o] = '='
            z -= 1
        if stap == "V":
            kubus[h][z][o] = '_'
            z -= 1
        if stap == "U":
            kubus[h][z][o] = '#'
            z -= 1
            h += 1
        if stap == "D":
            kubus[h-1][z][o] = '#'
            z -= 1
            h -= 1
        if stap == "L":
            kubus[h][z][o] = '_'
            nrichting = "W"
            o -= 1
        if stap == "R":
            kubus[h][z][o] = '_'
            nrichting = "O"
            o += 1
    if richting == "O":
        if stap == "S":
            kubus[h][z][o] = '='
            o += 1
        if stap == "V":
            kubus[h][z][o] = '_'
            o += 1
        if stap == "U":
            kubus[h][z][o] = '/'
            o += 1
            h += 1
        if stap == "D":
            kubus[h-1][z][o] = '\\'
            o += 1
            h -= 1
        if stap == "L":
            kubus[h][z][o] = '_'
            nrichting = "N"
            z -= 1
        if stap == "R":
            kubus[h][z][o] = '_'
            nrichting = "Z"
            z += 1
    if richting == "Z":
        if stap == "S":
            kubus[h][z][o] = '='
            z += 1
        if stap == "V":
            kubus[h][z][o] = '_'
            z += 1
        if stap == "U":
            kubus[h][z][o] = '#'
            z += 1
            h += 1
        if stap == "D":
            kubus[h-1][z][o] = '#'
            z += 1
            h -= 1
        if stap == "L":
            kubus[h][z][o] = '_'
            nrichting = "O"
            o += 1
        if stap == "R":
            kubus[h][z][o] = '_'
            nrichting = "W"
            o -= 1
    if richting == "W":
        if stap == "S":
            kubus[h][z][o] = '='
            o -= 1
        if stap == "V":
            kubus[h][z][o] = '_'
            o -= 1
        if stap == "U":
            kubus[h][z][o] = '\\'
            o -= 1
            h += 1
        if stap == "D":
            kubus[h-1][z][o] = '/'
            o -= 1
            h -= 1
        if stap == "L":
            kubus[h][z][o] = '_'
            nrichting = "Z"
            z += 1
        if stap == "R":
            kubus[h][z][o] = '_'
            nrichting = "N"
            z -= 1
    return ((h, z, o), nrichting, kubus)


n = int(input())
for k in range(n):
    _, eenstring = str(input()).split(' ')
    kubus = {}
    for i in range(len(eenstring) + 10):
        kubus[i] = {}
        for j in range(len(eenstring) + 10):
            kubus[i][j] = {}

    locatie = (len(eenstring) // 2, len(eenstring) // 2, len(eenstring) // 2)
    richting = 'O'
    mino, maxo, minh, maxh = len(eenstring) // 2, len(eenstring) // 2, len(eenstring) // 2, len(eenstring) // 2
    for letter in eenstring:
        locatie, richting, kubus = stap(richting, locatie, kubus, letter)
        if locatie[0] > maxh:
            maxh = locatie[0]
        if locatie[0] < minh:
            minh = locatie[0]
        if locatie[2] > maxo:
            maxo = locatie[2]
        if locatie[2] < mino:
            mino = locatie[2]

    for h in range(maxh, minh - 1, -1):
        print("{} ".format(k + 1), end='')
        for o in range(mino, maxo + 1):
            huidig = '.'
            for z in range(len(eenstring) + 10):
                if o in kubus[h][z]:
                    huidig = kubus[h][z][o]
            print(huidig, end='')
        print("")
