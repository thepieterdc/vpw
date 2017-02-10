lucky = {1}

for i in range(int(input())):
    num = int(input())
    if num in lucky:
        print("JA")
    else:
        l = set()
        while True:
            num = str(num)
            num = sum([int(x) * int(x) for x in num])
            if num in l:
                print("NEE")
                break
            l.add(num)
            if num in lucky:
                lucky = lucky.union(l)
                print("JA")
                break
