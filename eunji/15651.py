import sys
input = sys.stdin.readline
n,m = map(int,input().split())

result = [0]*10

def promising(result,i):
    switch = True
    return switch

def nandm(i):
    if promising(result,i):
        if i==m:
            print(*[result[k] for k in range(1,m+1)])
        else:
            for j in range(1,n+1):
                result[i+1] = j
                nandm(i+1)

nandm(0)