import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for x in B:
    print(1) if x in A else print(0)
