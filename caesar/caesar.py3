alf = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cases = int(input())
for i in range(cases):
    inp = str(input())
    inp = inp.split(" ",1)
    c = int(inp[0])
    zin = inp[1]
    for x in zin:
        if not alf.__contains__(x):
            print(x,end="")
        else:
            print(alf[(alf.index(x) - c)%27],end="")
    print()
