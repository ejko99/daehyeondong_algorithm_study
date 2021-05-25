# 개선된 backtracking algorithm

import sys
input = sys.stdin.readline

N = int(input())

arr = {}

count = 0

def promising(arr,i):
    flag = True
    for j in range(1,i):
        if arr[j]==arr[i] or i-j == abs(arr[i]-arr[j]):
            flag = False
    return flag

def nqueen(i):
    for k in range(1,N+1):
        arr[i+1] = k
        if promising(arr,i+1):
            if i+1==N:
                global count
                count += 1
            else:
                nqueen(i+1)

nqueen(0)
print(count)