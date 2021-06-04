import sys
from collections import Counter

n = int(sys.stdin.readline())
a = Counter(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
result = []

for x in b:
    result.append(a[x]) if x in a else result.append(0)

print(' '.join(map(str, [result[x] for x in range(m)])))
