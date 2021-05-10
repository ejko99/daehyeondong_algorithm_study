import sys

input = sys.stdin.readline
N = int(input())

arr = [int(input()) for _ in range(N)]

average = round(sum(arr)/N)
if N != 1:
    mid = (sorted(arr))[int(N/2)]
else:
    mid = arr[0]
ran = (sorted(arr))[-1] - (sorted(arr))[0]

mode_num = 0
arr_num_neg = [0]*4001
arr_num_pos = [0]*4000
arr_num = []

for i in range(N):
    if arr[i] <= 0:
        arr_num_neg[4000+arr[i]] += 1
    else:
        arr_num_pos[arr[i]-1] += 1
arr_num = arr_num_neg + arr_num_pos
max_arr = []
for i in range(8001):
    if arr_num[i]==max(arr_num):
        max_arr.append(i)

mode_index = max_arr[0]
if len(max_arr)>1:
    mode_index = max_arr[1]

if mode_index!=0:
    mode = mode_index-4000
else:
    mode = 0

print(average)
print(mid)
print(mode)
print(ran)