import string

n = int(input())
for cases in range(n):
    aantalpersons, aantallocaties, aantalwapens = (int(x) for x in str(input()).split(' '))
    aantalbevragingen = int(input())
    wels = [[], [], [], []]
    niets = [[], [], [], []]

    for vraag in range(aantalbevragingen):
        s, plw, e = str(input()).split(' ')

        if e == 'X':
            e = s

        s = int(s)
        s -= 1
        e = int(e)
        e -= 1
        if e <= s:
            e += 4
        if e != s-1:
            for i in range(s, e):
                niets[i % 4].append(plw)
        wels[e % 4].append(plw)


    print(wels)
    print(niets)
    for k in range(4):
        for l in range(len(wels[k])):
            joins = "".join(niets[k])
            for n in joins:
                x = []
                for a in wels[k][l]:
                    x.append(a.replace(n, ''))
                wels[k][l] = x
    for wel in range(4):
        pk = "a"
        for wel2 in wels[wel]:
            pk += "".join(wel2)
        print(pk)