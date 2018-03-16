import string

aantalcases = int(input())
for case in range(aantalcases):
    b, h = (int(i) for i in input().split(" "))

    grid = []

    startpt = 999999999999999999999999

    for hi in range(h):
        hoogtes = [int(i) for i in input().split(" ")]
        grid.append(hoogtes)

    currentpos = (0, 0)
    currentmin = 9999999999999999999999

    for hoogte in range(len(grid)):
        for breedte in range(len(grid[hoogte])):
            if grid[hoogte][breedte] < currentmin:
                currentmin = grid[hoogte][breedte]
                currentpos = (hoogte, breedte)

    wandeling = [currentpos]

    while True:
        currenthoogte, currentbreedte = currentpos

        nextmin = 99999999999999999999999999999
        nextpos = currentpos

        # boven
        if currenthoogte > 0 and currentmin < grid[currenthoogte - 1][currentbreedte] < nextmin:
            nextmin = grid[currenthoogte - 1][currentbreedte]
            nextpos = (currenthoogte - 1, currentbreedte)

        # onder
        if currenthoogte < h - 1 and currentmin < grid[currenthoogte + 1][currentbreedte] < nextmin:
            nextmin = grid[currenthoogte + 1][currentbreedte]
            nextpos = (currenthoogte + 1, currentbreedte)

        # links
        if currentbreedte > 0 and currentmin < grid[currenthoogte][currentbreedte - 1] < nextmin:
            nextmin = grid[currenthoogte][currentbreedte - 1]
            nextpos = (currenthoogte, currentbreedte - 1)

        # rechts
        if currentbreedte < b - 1 and currentmin < grid[currenthoogte][currentbreedte + 1] < nextmin:
            nextmin = grid[currenthoogte][currentbreedte + 1]
            nextpos = (currenthoogte, currentbreedte + 1)

        if nextpos == currentpos:
            break

        currentpos = nextpos
        currentmin = nextmin
        wandeling.append(nextpos)

    letters = string.ascii_uppercase

    for rij in range(h):
        print("{} ".format(case + 1), end="")
        for kol in range(b):
            try:
                pos = next(i for i in range(len(wandeling)) if (wandeling[i][0], wandeling[i][1]) == (rij, kol))
                print(letters[pos], end="")
            except StopIteration:
                print(".", end="")
        print("\n", end="")
