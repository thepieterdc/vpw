for idx in range(int(input())):
    n = int(input())

    getallen = set()
    uniekeset = set()
    for lijn in range(n):
        a, b = tuple(map(int, input().split(" ")))
        uniekeset = set()
        getallen.add((a, b))
        getallen.add((b, a))

    allepunten = {x[0] for x in getallen}

    heeftcykels = False
    start = 1


    puntenGezien = {start}

    for _ in range(1000):
        puntenGezienVeranderd = False
        for punt in allepunten:
            if punt in puntenGezien:
                continue

            burenVanPunt = {p[0] for p in getallen if p[1] == punt}
            intersectie = burenVanPunt & puntenGezien
            if len(intersectie) == 1:
                puntenGezien.add(punt)
                puntenGezienVeranderd = True
            elif len(intersectie) >= 2:
                heeftcykels = True
                break

        if not puntenGezienVeranderd or heeftcykels:
            break

    if not heeftcykels:
        outputs = list(getallen)
        outputs.sort()
        output = ' '.join(f"({x[0]},{x[1]})" for x in outputs)
        print(f"{idx + 1} {output if output else 'geen'}")

    else:
        dood = []
        doodl = -1
        outputs = []
        while len(dood) != doodl:
            doodl = len(dood)
            for i in range(1, n + 1):
                if i not in dood:
                    b = {t for t in getallen if t[0] == i}
                    bl = {t for t in b if t[1] not in dood}
                    if len(bl) <= 1:
                        dood.append(i)
                        nieuw = {x for x in getallen if x[0] not in dood and x[1] == i}
                        outputs.extend(nieuw)

        outputs.sort()
        output = ' '.join(f"({x[0]},{x[1]})" for x in outputs)
        print(f"{idx+1} {output if output else 'geen'}")
