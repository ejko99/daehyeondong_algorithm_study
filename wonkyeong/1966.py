import sys
from collections import deque

idx = 0
cnt = 0
n = int(sys.stdin.readline())

for i in range(n):
    q = list(map(int, sys.stdin.readline().split()))
    imp = [int(sys.stdin.readline() for _ in range(q[0]))]
    imp = deque(imp)

    while(1):
        if imp[0] == max(imp):
            cnt += 1
            q[1] -= 1
            if idx = q[1]:
                break
        else:
            imp.rotate(-1)
            idx += 1
            
    
