# counting sort

import sys
input = sys.stdin.readline
N = int(input())

counting_arr = [0]*10001
for i in range(N):
    counting_arr[int(input())] += 1

for i in range(1,10001):
    while counting_arr[i] != 0:
        print(i)
        counting_arr[i]-=1