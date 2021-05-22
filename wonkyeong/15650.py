import sys

m, n = map(int, sys.stdin.readline().split())
ans = []
visited = [False for _ in range(m)]


def backtracking(depth, n, m):

    if depth == n and ans == sorted(ans):
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1, m+1):
        #print(ans)
        if not visited[i-1]:
            visited[i-1] = True
            ans.append(i)
            backtracking(depth+1, n, m)
            visited[i-1] = False
            ans.pop()

backtracking(0, n, m)
