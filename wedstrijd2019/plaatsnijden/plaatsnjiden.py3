import functools


def m(x, y) -> tuple:
    return max(x, y), min(x, y)


def snijd(x, y):
    stukken = dict()
    stukken[m(x, y)] = 1
    return snijd_rec(stukken, 0)


def snijd_rec(stukken: dict, r2):
    r = len(stukken)
    startr = r
    if r < r2:
        return 0
    for s in stukken.keys():
        st = stukken.copy()
        st[s] -= 1
        if not st[s]:
            del st[s]
        for i in range(1, (s[0] // 2) + 1):
            st2 = st.copy()
            if m(i, s[1]) in st2:
                st2[m(i, s[1])] += 1
            else:
                st2[m(i, s[1])] = 1

            if m(s[0] - i, s[1]) in st2:
                st2[m(s[0] - i, s[1])] += 1
            else:
                st2[m(s[0] - i, s[1])] = 1

            r = max(r, snijd_rec(st2, startr))

        for i in range(1, (s[1] // 2) + 1):
            st2 = st.copy()
            if m(i, s[0]) in st2:
                st2[m(i, s[0])] += 1
            else:
                st2[m(i, s[0])] = 1

            if m(s[1] - i, s[0]) in st2:
                st2[m(s[1] - i, s[0])] += 1
            else:
                st2[m(s[1] - i, s[0])] = 1

            r = max(r, snijd_rec(st2, startr))

    return r


for ni in range(int(input())):
    x, y = map(int, input().split(" "))
    print("{} {}".format(ni + 1, snijd(x, y)))
