import sys
from itertools import permutations

maxnum, n = map(int, sys.stdin.readline().split())
l = permutations(range(1, maxnum+1), n)

for i in l:
    print(' '.join(map(str,i)))
