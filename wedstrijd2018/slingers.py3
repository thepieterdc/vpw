from collections import Counter


def slinger(tekst):
    tekst = list(tekst)
    sterren = [i for i in range(len(tekst)) if tekst[i] == "*"]
    delta = [sterren[i + 1] - sterren[i] for i in range(len(sterren) - 1)]

    if not delta:
        return tekst

    if len(delta) == 1:
        d = delta[0]
        if sterren[0] >= d:
            tekst[sterren[0]] = "."
        elif len(tekst) - sterren[-1] >= d:
            tekst[sterren[-1]] = "."
        return tekst

    c = Counter(delta)
    csort = c.most_common()
    maxc = csort[0][0]

    if '*' not in tekst:
        return tekst

    if len(c) == 1:
        if sterren[0] >= maxc:
            tekst[sterren[0] - maxc] = "*"
        elif len(tekst) - sterren[-1] > maxc:
            tekst[sterren[-1] + maxc] = "*"
        return tekst
    else:
        if len(csort) == 2:
            l = delta.index(csort[1][0])
            if l == 0:
                tekst[sterren[l]] = "."

            elif (csort[1][0]) == 2*csort[0][0]:
                l = delta.index(csort[1][0])
                tekst[sterren[l] + maxc] = '*'
            else:
                l = delta.index(csort[1][0])
                tekst[sterren[l+1]] = '.'
        else:
            l = max(delta.index(csort[1][0]), delta.index(csort[2][0]))
            tekst[sterren[l]] = '.'
        return tekst


for case in range(int(input())):
    _ = input()
    tekst = str(input())
    print("{} {}".format(case + 1, "".join(slinger(tekst))))
