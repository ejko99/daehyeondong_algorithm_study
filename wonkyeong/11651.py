import sys

l = []
N = int(sys.stdin.readline())

for i in range(N):
    x, y = map(int, (sys.stdin.readline().split()))
    l.append((y, x))
l.sort()

for y, x in l:
    print(str(x) + " " + str(y))
