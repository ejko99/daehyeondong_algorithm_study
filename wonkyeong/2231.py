import sys

n = int(sys.stdin.readline())
leng = len(str(n))

for x in range(max(n-(leng*9),0), n):
    l = [int(str(x)[i]) for i in range(len(str(x)))]
    if (int(x)+sum(l)) == n:
        print(x)
        break
    elif (x==n-1):
        print(0)
