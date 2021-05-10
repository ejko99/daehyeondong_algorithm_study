import sys

l = []
N = int(sys.stdin.readline())

for i in range(N):
    x, y = map(int, (sys.stdin.readline().split()))
    l.append((x, y))
l.sort()

for x, y in l:
    print(str(x) + " " + str(y))
