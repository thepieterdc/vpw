from collections import Counter, defaultdict


def case(matrix1, matrix2):
    swaps1 = swapSets(matrix1)
    swaps2 = swapSets(matrix2)

    count = 0
    for i in ((0, 0), (1, 0), (0, 1), (1, 1)):
        sets1 = swaps1[i]
        sets2 = swaps2[i]
        for (item1, count1) in sets1.items():
            count += max(0, sets2[item1] - count1)

    return count

def swapSets(matrix):
    sets = defaultdict(Counter)
    for ridx, r in enumerate(matrix):
        for cidx, cell in enumerate(r):
            if cell not in {'*', '.'}:
                sets[(ridx % 2, cidx % 2)][cell] += 1
    return sets

for idx in range(int(input())):
    columns, rows = tuple(map(int, input().split(" ")))
    matrix1 = []
    for _ in range(rows):
        matrix1.append(list(input()))

    matrix2 = []
    for _ in range(rows):
        matrix2.append(list(input()))

    print(f"{idx + 1} {case(matrix1, matrix2)}")