# import operator
#
# best = 99999999999999999999
#
#
# def afstand(huis1: tuple, huis2: tuple):
#     huis1x, huis1y = huis1
#     huis2x, huis2y = huis2
#
#     return abs(huis1x - huis2x) + abs(huis1y - huis2y)
#
#
# def jacht(gekozen: set, vrij: set, m: int, k: int, dist: int):
#     global best
#
#     if k == 0:
#         best = min(best, dist)
#
#     if not vrij:
#         return
#
#     for (volg, (x, y)) in vrij:
#         if volg > m:
#             for (x2, y2) in gekozen:
#                 dist = max(dist, afstand((x, y), (x2, y2)))
#
#             jacht(gekozen | {(x, y)}, vrij - {(x, y)}, volg, k - 1, dist)
#
#
# for ni in range(int(input())):
#     totaalhuizen, n = map(int, input().split(" "))
#
#     huizen = set()
#
#     for ki in range(totaalhuizen):
#         x, y = map(int, input().split(" "))
#         huizen.add(tuple((ki, (x, y))))
#
#     best = 99999999999999999999
#     jacht(set(), huizen, -1, n, 0)
#
#     print("{} {}".format(ni + 1, best))
import functools
import operator


@functools.lru_cache(500000)
def afstand(huis1: tuple, huis2: tuple):
    huis1x, huis1y = huis1
    huis2x, huis2y = huis2

    return abs(huis1x - huis2x) + abs(huis1y - huis2y)


def rec(left: set, current: set, n: int):
    if n == 0:
        return current

    if n == len(left):
        return left | current

    best = min({(huis, max(afstand(huis, huisCurrent) for huisCurrent in current)) for huis in left},
               key=operator.itemgetter(1))

    return rec(left - {best[0]}, current | {best[0]}, n - 1)


for ni in range(int(input())):
    totaalhuizen, n = map(int, input().split(" "))

    huizen = set()

    for ki in range(totaalhuizen):
        x, y = map(int, input().split(" "))
        huizen.add(tuple((x, y)))

    gs = 9999999999999999999999999999
    for first in huizen:
        res = rec(huizen - {first}, {first}, n - 1)
        gs = min(gs, max(afstand(huis, anderhuis) for huis in res for anderhuis in res if huis != anderhuis))

    print("{} {}".format(ni + 1, gs))
