import sys

input = sys.stdin.readline
N = int(input())

s = set()
[s.add(input().rstrip('\n')) for _ in range(N)]

arr = sorted(list(s)) # 이부분 꼭 필요 (sorted는 안정정렬)

arr2 = []
for sent in arr:
    arr2.append([sent,len(sent)])
arr2 = sorted(arr2,key=lambda arr:arr[1])

[print(arr2[i][0]) for i in range(len(arr2))]