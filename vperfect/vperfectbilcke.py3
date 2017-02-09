import math

def isvshit(i):
    som = 0
    for k in range(1,math.floor(math.sqrt(i))+1):
        if(i%(k) == 0):
            som += k
            if(k*k != i):
                som += i/k
    if som%i == 0:
        #returnt v !
        return som/i
    return 0

n = int(input())
for p in range(n):
    xy = input().split(' ')
    x,y = xy
    i = int(x)
    b = True
    v = 0
    while (b and i<int(y)):
        v = isvshit(i)
        if v != 0:
            b = False
        i += 1
    if not b:
        #dit kan eleganter? :)
        print(str(i-1) + ' ' + str(int(v)))
    else:
        print("GEEN")
