N = int(input())

arr = [0]*15
count = 0

def promising(arr,i):
    flag = True
    for j in range(i):
        if arr[j]==arr[i] or i-j == abs(arr[i]-arr[j]):
            flag = False
    return flag


def nqueen(i):
    if promising(arr,i):
        if i==N:
            count =+ 1
            print(count)
        else:
            for k in range(N):
                arr[i+1] = k
            nqueen(i+1)

nqueen(0)
print(count)