N = int(input())

arr = [0]*15
count = 0

def promising(arr,i):
    flag = True
    for j in range(1,i):
        if arr[j]==arr[i] or i-j == abs(arr[i]-arr[j]):
            flag = False
            break
    return flag

def nqueen(i):
    if promising(arr,i):
        if i==N:
            global count
            count += 1
        else:
            for k in range(1,N+1):
                arr[i+1] = k
                nqueen(i+1)

nqueen(0)
print(count)