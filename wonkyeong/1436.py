import sys

N = int(sys.stdin.readline())
cnt = 0
title = 665


while(1):
    title += 1
    if '666' in str(title):
        cnt += 1
    if cnt == N:
        print(title)
        break