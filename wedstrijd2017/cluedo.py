import string

n = int(input())
for k in range(n):
    aantalpersons, aantallocaties, aantalwapens = (int(x) for x in str(input()).split(' '))
    aantalbevragingen = int(input())
    spelers = []
    for i in range(4):
        spelers.append([[], list(string.ascii_uppercase[:aantallocaties]),
                        list(string.ascii_lowercase[:aantalwapens])])

        for j in range(4):
            spelers[i][0].append(str(j + 1))

    zeker = [[], [], [], []]

    def verwijderen(speler, kaart, groep):
        return
        for nieuwei in range(0, 4):
            if nieuwei != speler:
                if kaart in spelers[nieuwei][groep]:
                    spelers[nieuwei][groep].remove(kaart)
                    for lengteZeker in range(len(zeker[nieuwei])):
                        if kaart in zeker[nieuwei][lengteZeker]:
                            zeker[nieuwei][lengteZeker].replace(kaart, '')
                            if len(zeker[nieuwei][lengteZeker]) == 1:
                                if zeker[nieuwei][lengteZeker] in ['1','2','3','4','5','6','7','8','9']:
                                    groep = 0
                                elif zeker[nieuwei][lengteZeker] in string.ascii_uppercase:
                                    groep = 1
                                elif zeker[nieuwei][lengteZeker] in string.ascii_lowercase:
                                    groep = 2
                                verwijderen(nieuwei, zeker[nieuwei][lengteZeker], groep)


    for i in range(aantalbevragingen):
        startperson, kaarten, eindperson = str(input()).split(' ')

        startperson = int(startperson)
        if eindperson != "X":
            eindperson = int(eindperson)
            person = (startperson + 1) % 5
            if person == 0:
                person = 1
            while person != eindperson:
                for i in range(0, 3):
                    if str(kaarten[i]) in spelers[person - 1][i]:
                        spelers[person - 1][i].remove(str(kaarten[i]))
                person = (person + 1) % 5
                if person == 0:
                    person = 1
            wss = ''
            for groep in range(0, 3):
                if kaarten[groep] in spelers[eindperson - 1][groep] and kaarten[groep] not in zeker[eindperson-1]:
                    wss += kaarten[groep]
            zeker[eindperson-1].append(wss)

            if len(wss) == 1:
                if wss in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    groep = 0
                elif wss in string.ascii_uppercase:
                    groep = 1
                elif wss in string.ascii_lowercase:
                    groep = 2
                verwijderen(eindperson - 1, wss, groep)
        else:
            for o in range(4):
                for x in range(3):
                    if str(kaarten[x]) in spelers[o][x] and o != startperson - 1:
                        spelers[o][x].remove(str(kaarten[x]))

                        # eindperson = int(eindperson)
                        # if eindperson > startperson:
                        #     for speler in range(startperson, eindperson - startperson +1):
                        #         for o in range(3):
                        #             if str(kaarten[o]) in spelers[speler][o]:
                        #                 spelers[speler][o].remove(str(kaarten[o]))
                        # else:
                        #     for speler in range(0, 4):
                        #         if startperson-1 > speler > eindperson-1:
                        #             for o in range(3):
                        #                 if str(kaarten[o]) in spelers[speler][o]:
                        #                     spelers[speler][o].remove(str(kaarten[o]))
                        # else:
                        # for o in range(4):
                        #     for x in range(3):
                        #         if str(kaarten[x]) in spelers[o][x] and o != startperson:
                        #             spelers[o][x].remove(str(kaarten[x]))

        print("{} {} {}".format(i, kaarten, spelers))
    print(zeker)
    print("{} {} {} {} {}".format(k + 1, "".join(spelers[0][0] + spelers[0][1] + spelers[0][2]),
                                  "".join(spelers[1][0] + spelers[1][1] + spelers[1][2]),
                                  "".join(spelers[2][0] + spelers[2][1] + spelers[2][2]),
                                  "".join(spelers[3][0] + spelers[3][1] + spelers[3][2])))
