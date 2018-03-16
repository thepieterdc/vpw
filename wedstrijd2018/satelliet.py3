optoplossing = ""


def back(signaal, opl, map):
    # print(signaal)
    global optoplossing

    if not signaal and (len(optoplossing) > len(opl) or not optoplossing):
        optoplossing = opl
    if not signaal and len(optoplossing) == len(opl) and opl < optoplossing:
        optoplossing = opl

    if not signaal:
        return

    woord = signaal[0]
    i = 0
    while len(woord) < len(signaal) + 1:
        while woord not in map and i < len(signaal) - 1:
            i += 1
            woord += signaal[i]

        if woord not in map:
            return

        opl2 = opl + map[woord]

        if i + 1 != len(signaal):
            signaal2 = signaal[i + 1:]
        else:
            signaal2 = ""

        back(signaal2, opl2, map)
        i += 1

        if i < len(signaal):
            woord += signaal[i]

        if i >= len(signaal):
            return


for case in range(int(input())):
    signaal = list(str(input()))
    aantal_lettercodes = int(input())

    optoplossing = ""

    map = dict()
    for i in range(aantal_lettercodes):
        letter = str(input())
        code = str(input())
        map[code] = letter

    back(signaal, "", map)

    if not optoplossing:
        print("{} ONMOGELIJK".format(case + 1))
    else:
        print("{} {}".format(case + 1, "".join(optoplossing)))
