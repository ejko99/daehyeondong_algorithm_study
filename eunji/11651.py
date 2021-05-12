import sys

input = sys.stdin.readline
N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
arr = sorted(arr,key = lambda arr: arr[0] + 10000000*arr[1])
for i in range(N):
    print(str(arr[i][0])+' '+str(arr[i][1]))