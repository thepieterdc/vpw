def run(beginKapitaal, bedragen: list[int]) -> int:
    if not bedragen:
        return beginKapitaal

    aantalAandelen = 0
    geld = beginKapitaal
    for idx, huidigeValue in enumerate(bedragen[:-1]):
        volgendeValue = bedragen[idx + 1]

        if volgendeValue < huidigeValue:
            geld += aantalAandelen * huidigeValue
            aantalAandelen = 0
        elif volgendeValue > huidigeValue:
            aantalAandelenGekocht = geld // huidigeValue
            aantalAandelen += aantalAandelenGekocht
            geld -= aantalAandelenGekocht * huidigeValue

    if aantalAandelen:
        geld += aantalAandelen * bedragen[-1]

    return geld


for idx in range(int(input())):
    beginKapitaal = int(input())
    aantal = int(input())
    bedragen = [int(x) for x in input().split(" ") if x]
    print(f"{idx + 1} {run(beginKapitaal, bedragen)}")
