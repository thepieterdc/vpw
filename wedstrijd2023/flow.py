maxSeenLength = 0


def backtrack(buren: dict[int, set], seen, todo: set):
    global maxSeenLength

    if not todo:
        maxSeenLength = max(maxSeenLength, len(seen))
        return len(seen)

    n = todo.pop()
    if len(seen) + len(todo) + 1 < maxSeenLength:
        return 0

    burenVanN = buren[n]
    if burenVanN & seen:
        wel = 0
    else:
        wel = backtrack(buren, seen | {n}, todo - burenVanN)

    niet = backtrack(buren, seen, todo)
    return max(wel, niet)


def run(matrix: list[list[int]], rows, columns) -> int:
    global maxSeenLength
    maxSeenLength = 0

    maxGetal = max(g for row in matrix for g in row)
    buren = {n + 1: set() for n in range(maxGetal)}
    startEndPunten = set()

    for r in range(rows):
        for c in range(columns):
            m = matrix[r][c]

            buurCoordinaten = {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}
            buurCoordinaten = {(r_, c_) for (r_, c_) in buurCoordinaten if 0 <= r_ < rows and 0 <= c_ < columns}
            heeftZichZelfMeerDan1KeerAlsBuur = sum(1 for (r_, c_) in buurCoordinaten if matrix[r_][c_] == m) > 1

            if not heeftZichZelfMeerDan1KeerAlsBuur:
                startEndPunten.add((r, c))

    for (r, c) in startEndPunten:
        matrix[r][c] = 0

    for r in range(rows):
        for c in range(columns):
            m = matrix[r][c]
            for (dr, dc) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= (r + dr) < len(matrix) and 0 <= (c + dc) < len(matrix[r]):
                    buur = matrix[r + dr][c + dc]
                    if buur != m and buur * m != 0:
                        buren[m].add(buur)
                        buren[buur].add(m)

    result = backtrack(buren, set(), set(range(1, maxGetal + 1)))
    return result


for idx in range(int(input())):
    matrix = []
    rows, columns = tuple(map(int, input().split(" ")))
    for _ in range(rows):
        matrix.append(list(map(int, input().split(" "))))

    print(f"{idx + 1} {run(matrix, rows, columns)}")
