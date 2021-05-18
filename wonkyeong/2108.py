import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]
l.sort()
maxcnt = n

print(int(sum(l)/n))
print(l[(n//2) + 1])
for i in l:
    maxcnt = max(maxcnt, l.count(i))
print()
