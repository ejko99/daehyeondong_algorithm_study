import sys

n = sys.stdin.readline()[:-1]
length = len(n)
l = list(n)
l.sort(reverse=True)

for i in range(length):
    print(l[i], end="")
