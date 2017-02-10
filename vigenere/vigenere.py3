import itertools


def encode(key, raw):
    key = itertools.cycle(key)
    return "".join([letter((value(i) + value(next(key, None))) % 27) for i in raw])


def decode(key, enc):
    key = itertools.cycle(key)
    return "".join([letter((value(i) - value(next(key, None)) + 27) % 27) for i in enc])


def letter(i):
    return ' ' if i == 0 else chr(64 + i)


def value(l):
    return ord(l) - 64 if not l.isspace() else 0


for ei in range(int(input())):
    print(encode(*str(input()).split(' ', 1)))
for di in range(int(input())):
    print(decode(*str(input()).split(' ', 1)))
