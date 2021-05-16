import sys

input = sys.stdin.readline
N = int(input())

arr = list(map(int,input().split()))
arr_uniq = sorted(list(set(arr)))

arr_2dim = {arr_uniq[i]:i for i in range(len(arr_uniq))}

print(*[arr_2dim[i] for i in arr])