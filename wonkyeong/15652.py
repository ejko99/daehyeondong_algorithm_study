import sys

m, n = map(int, sys.stdin.readline().split())
ans = []

def backtracking(depth, n, m):

    if depth == n:
        print(" ".join(map(str, ans)))
        return

    if ans != []:
        k = ans[-1]
    else:
        k = 1

    for i in range(k, m+1):
        ans.append(i)
        backtracking(depth+1, n, m)
        ans.pop()

backtracking(0, n, m)
