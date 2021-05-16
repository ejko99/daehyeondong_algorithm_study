import sys

n = int(sys.stdin.readline())
l = [int(x) for x in sys.stdin.readline().split()]
ans = [0 for _ in range(n)]

for i, x in enumerate(l):
    if x in l[:i]:
        break
    tmp = [e > x for e in l]
    ans = [sum(x) for x in zip(tmp, ans)]

for x in n:
    print(ans[x], end=" ")
