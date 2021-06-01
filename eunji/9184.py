import sys

input = sys.stdin.readline

arr = [[[0]*20]*20]*20
print(arr)


while(1):
    nums = list(map(int,input().split()))
    if nums == [-1,-1,-1]:
        break
