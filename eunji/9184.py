import sys

input = sys.stdin.readline

w = [[[1]*21]*21]*21

# def recur(a,b,c):
#     if a<=0 or b<=0 or c<=0:
#         return 1
#     # elif a>20 or b>20 or c>20:
#     #     w[a][b][c] = w[20][20][20]
#     #     return recur(20,20,20)
#     elif a<b and b<c:
#         w[a][b][c] = recur(a,b,c-1) + recur(a,b-1,c-1) - recur(a,b-1,c)
#         return w[a][b][c]
#     else:
#         w[a][b][c] = recur(a-1,b,c) + recur(a-1,b-1,c) + recur(a-1,b,c-1) - recur(a-1,b-1,c-1)
#         return w[a][b][c]

for a in range(1,21):
    for c in range(1,21):
        for b in range(1,21):
            if a<b and b<c:
                w[a][b][c] = w[a][b][c-1] + w[a][b-1][c-1] - w[a][b-1][c]
            else:
                w[a][b][c] = w[a-1][b][c] + w[a-1][b-1][c] + w[a-1][b][c-1] - w[a-1][b-1][c-1]

while(1):
    nums = list(map(int,input().split()))
    print(nums)
    if nums == [-1,-1,-1]:
        break
    elif nums[0]<=0 or nums[1]<=0 or nums[2]<=0:
        print('first elif :',1)
    elif nums[0]>20 or nums[1]>20 or nums[2]>20:
        print('second elif :',w[20][20][20])
    else:
        print('last else :',w[nums[0]][nums[1]][nums[2]])