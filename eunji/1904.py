import sys

input = sys.stdin.readline
num = int(input())

if num==1:
    print(1)

# arr = [[1]*num for _ in range(num)]

# for i in range(2,num+1):
#     for j in range(1,i):
#         arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

# ans = 0

# for i in range(int(num/2) + 1):
#     ans += arr[num-i][i]
#     print(ans%15746)


even = [1]*num
odd = [1]*num

ans = 0

for i in range(2,num+1):
    if i%2 == 0:
        for j in range(1,i):
            even[j] = odd[j-1]+odd[j]
        print(even)
    else:
        for j in range(1,i):
            odd[j] = even[j-1]+even[j]
        print(odd)
    # how to get index?
    if num%2 == 0 and i== num-int(num/2):
        for k in range(int(num/2)+2):
            if (num-int(num/2))%2:
                ans+=even[num-int(num/2)]
            else:
                ans+=odd[num-int(num/2)]
