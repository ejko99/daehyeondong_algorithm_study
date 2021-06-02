import sys
import collections

n, m = map(int, sys.stdin.readline().split())
l = map(int, sys.stdin.readline().split())
q = collections.deque([x for x in range(1, n+1)])
count = 0

for i in l:
    if q.index(i) <= n/2:
        while q.index(i) != 0:
            q.rotate(-1)
            count += 1
        q.popleft()
    else:
        while q.index(i) != 0:
            q.rotate(1)
            count += 1
        q.popleft()
    n -= 1

print(count)
