for idx in range(int(input())):
    line = input().split(" ")
    moves = []
    for i in range(0, len(line), 2):
        moves.append((int(line[i]), line[i + 1]))

    richtingen = {'N': (1, 0), 'O': (0, 1), 'Z': (-1, 0), 'W': (0, -1)}

    pad = [(0, 0)]
    loc = (0, 0)
    kruispuntLocaties = {}
    kruispunten = set()
    for (n, richt) in moves:
        while n > 0:
            dx, dy = richtingen[richt]
            x, y = loc
            loc = (x + dx, y + dy)
            if loc in pad:
                kruispunten.add(loc)
                kruispuntLocaties[loc] = (pad.index(loc), len(pad))
            pad.append(loc)
            n -= 1

    while kruispunten:
        reversePad = list(reversed(pad))
        locAfstanden = []
        for (kruispunt, (x, y)) in kruispuntLocaties.items():
            locAfstanden.append((abs(x - y), kruispunt, x, y))

        _, maxKruispunt, idxPad, idxReverse = max(locAfstanden)

        kruispuntLocaties.pop(maxKruispunt, None)
        nieuwKruispuntLocaties = {}
        for (kruispunt, (x,y)) in kruispuntLocaties.items():


        pad = pad[:idxPad + 1] + pad[idxReverse:]

    print(f"{idx + 1} {len(pad) - 1}")