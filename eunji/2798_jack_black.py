N,M = map(int,input().split())
arr = map(int,input().split())
min_num = M

for i in range(N-1):
    num1 = arr[i]
    for j in range(i+1,N):
        num2 = arr[j]
        for k in range(j+1,N):
            num3 = arr[k]

            number = num1+num2+num3
            if number>M:
                break
            if M-number<min_num:
                min_num = M-number

print(M-min_num)

