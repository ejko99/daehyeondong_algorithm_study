import sys

l = []
n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline()[:-1].split(' '))
    l.append([x, y, 1])

for i in l:
    rank = 1
    for j in l:
        if (i[0] < j[0]) and (i[1] < j[1]):
            i[2] += 1
    print(i[2], end=" ")
