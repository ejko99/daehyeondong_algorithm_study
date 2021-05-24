import sys

n = int(sys.stdin.readline().split())
l = [int(sys.stdin.readline().split()) for _ in range(n)]
m = [sys.stdin.readline().split() for _ in range(4)]
ans = []

def backtracking(depth, n, m):
    for i in range(l):
        ans.append(i)
        backtracking(depth+1, n, m)
        ans.pop()

backtracking(0, n, m)
