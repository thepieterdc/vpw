import string

optopl = []

def back(seq, opl, wissel, index):
    global optopl

    if seq == opl:
        if len(wissel) < len(optopl) or not optopl:
            optopl = wissel
            return True

    i = 0
    while i < len(seq) and seq[i] == opl[i]:
        i += 1

    if i < len(seq):
        found = False

        for j in range(i + 1, len(opl)):
            if opl[i] == seq[j]:
                seqcopy = list(seq)
                temp = seqcopy[i]
                seqcopy[i] = seqcopy[j]
                seqcopy[j] = temp
                wissel2 = wissel.copy()
                wissel2.append((i + index, j + index))
                found = back(seqcopy[i + 1:], opl[i + 1:], wissel2, index + i + 1)

        return found
    else:
        return True


for case in range(int(input())):
    sequentie = list(input())
    oplossing = list(input())

    optopl = []

    ret = back(sequentie, oplossing, [], 0)

    letters = string.ascii_uppercase
    if ret and optopl:
        oplossing = [x for tup in optopl for x in tup]
        oplossing = "".join(letters[x] for x in oplossing)
        print("{} {}".format(case + 1, oplossing))
    elif ret:
        print("{} correct".format(case + 1))
    else:
        print("{} onmogelijk".format(case + 1))
