for c in range(int(input())):
    w, h = (int(x) for x in str(input()).split(' '))
    front = [str(input()) for _ in range(h)]
    _ = input()
    mask = [str(input()) for _ in range(h)]
    _ = input()
    back = [str(input()) for _ in range(h)]

    print("{} {}".format(w, h))
    for r in range(h):
        for k in range(w):
            print(front[r][k] if mask[r][k] == 'F' else back[r][k], end='')
        print("\n", end='')
