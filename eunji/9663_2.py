from itertools import permutations

N = int(input())

arr = []
[arr.append(i) for i in range(1,N+1)]

count = 0

for i in list(permutations(arr,N)):
    flag = True
    for j in range(N):
        for k in range(j):
            if j-k == abs(i[j]-i[k]):
                flag = False
                break
    if flag:
        count += 1

print(count)
