import sys

input = sys.stdin.readline
N = int(input())

zero_arr = [1,0]
one_arr = [0,1]

for _ in range(40):
    zero_arr.append(zero_arr[-1]+zero_arr[-2])
    one_arr.append(one_arr[-1]+one_arr[-2])

for _ in range(N):
    num = int(input())
    if num ==0:
        print(1,0)
    elif num==1:
        print(0,1)
    else:
        print(zero_arr[num],one_arr[num])