import sys

input = sys.stdin.readline
N = int(input())

arr = []

for i in range(N):
    age, name = map(str,input().split())
    arr.append([int(age),name])
arr = sorted(arr,key=lambda arr: arr[0])
[print(str(arr[i][0])+' '+arr[i][1]) for i in range(N)]