import sys

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n-1):
    for j in range(n-1-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(int(sum(l)/n))
print(l[int((n-1)/2)])
print(l[-1]-l[0])
