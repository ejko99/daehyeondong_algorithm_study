import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for i in range(n)]
l.sort()

for i in range(n):
    print(l[i])