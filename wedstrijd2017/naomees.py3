def nao(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-2] and s[1] == s[-1] and s[0:2] in ["ba", "di", "du"]:
        if(nao(s[2:-2])):
            return True
    l = len(s)
    if s[:l//2] == s[l//2:]:
        return nao(s[:l//2])
    return False

n = int(input())
for k in range(n):
    ret = ""
    for i in range(5):
        s = str(input())
        r = "naomees " if nao(s) else "onzin "
        ret += r
    print("{} {}".format(k+1, ret[:-1]))