import sys

m, n = map(int, sys.stdin.readline().split())
ans = []


def backtracking(depth, n, m):

    if depth == n:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1, m+1):
        ans.append(i)
        backtracking(depth+1, n, m)
        ans.pop()

backtracking(0, n, m)
