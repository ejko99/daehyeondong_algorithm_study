import sys

input = sys.stdin.readline

arr = [[[0]*20]*20]*20
print(arr)



while(1):
    nums = list(map(int,input().split()))
    if nums == [-1,-1,-1]:
        break
    if nums[0]>20 or nums[1]>20 or nums[2]>20:
        print(arr[20,20,20])
    if nums[0]<=0 or nums[1]<=0 or nums[2]<=0:
        print(1)
    else:
        print(arr[nums[0],nums[1],nums[2]])