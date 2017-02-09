cases = int(input())
for c in range(cases):
    nums = [int(input()) for _ in range(int(input()))]
    print("{} {} {}".format(c+1, min(nums), max(nums)))
