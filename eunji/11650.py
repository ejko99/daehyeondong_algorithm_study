# *****숫자 정렬할 때 str형태를 정렬하고 있지 않은지 주의*****

import sys

input = sys.stdin.readline
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
arr = sorted(arr)
for i in range(N):
    print(str(arr[i][0])+' '+str(arr[i][1]))