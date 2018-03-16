def juisteVerwacht(bedrag, resultaat, verwacht, munten):
    verwacht = list(sorted(verwacht))
    overschot = abs(bedrag)
    i = 0
    teruggave = []

    while overschot > 0 and i < len(munten):
        if overschot - munten[i] < 0:
            i += 1
        else:
            overschot -= munten[i]
            teruggave.append(munten[i])

    if overschot == 0 and list(sorted(teruggave)) == verwacht:
        return True
    return False


global globaalbezit


def vindbedrag(bedrag, bezit, resultaat, verwacht, munten, beste):
    if bedrag <= 0:
        if juisteVerwacht(bedrag, resultaat, verwacht, munten):
            beste = len(resultaat)
        return beste

    if len(resultaat) >= beste:
        return beste

    for i, munt in enumerate(bezit):
        resultaat.append(munt)
        res = vindbedrag(bedrag - munt, bezit[i + 1:], resultaat, verwacht, munten, beste)
        resultaat.remove(munt)
        if res != "ONMOGELIJK":
            if res < beste:
                beste = res

    if beste < len(globaalbezit) + 1:
        return beste

    return "ONMOGELIJK"


for ni in range(int(input())):
    bedrag = int(input())
    bezit = list(map(int, input().split(" ")))[1:]
    munten = list(map(int, input().split(" ")))[1:]
    verwacht = list(map(int, input().split(" ")))[1:]

    bezit = list(sorted(bezit))
    munten = list(sorted(munten, reverse=True))

    globaalbezit = list(bezit)

    print("{} {}".format(ni + 1, vindbedrag(bedrag, bezit, [], verwacht, munten, len(bezit) + 1)))
