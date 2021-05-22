n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)
print(a)
print(b)
print(c)

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]): #하나라도 True 있으면 True 
            a[j] = b[i+j] = c[i-j+n-1] = True
            print(i,j)
            print(a,end=' first a\n')
            print(b,end=' first b\n')
            print(c,end=' first c\n')
            print(i+1,end='\n')
            solve(i+1)
            print(i,j)
            print(a,end=' second a\n')
            print(b,end=' second b\n')
            print(c,end=' second c\n')
            a[j] = b[i+j] = c[i-j+n-1] = False
            print(i,j)
            print(a,end=' third a\n')
            print(b,end=' thrid b\n')
            print(c,end=' thrid c\n')
solve(0)
print(ans)


