import sys

N = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(N)]
arr = sorted(arr)

for i in range(N):
    print(arr[i])