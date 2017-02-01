for k in range(int(input())):
    num, denom = str(input()).split(' ')
    num, denom = list(num), list(denom)
    p, l = 0, min(len(num), len(denom))
    while p < l:
        try:
            denomp = denom.index(num[p])
            del num[p]
            del denom[denomp]
        except ValueError:
            p += 1
        except IndexError:
            break
    print("{} {}".format("".join(sorted(num)) if num else 1, "".join(sorted(denom)) if denom else 1))
