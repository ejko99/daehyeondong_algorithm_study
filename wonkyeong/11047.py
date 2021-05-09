import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
val = 0

for i in range(n):
    coin.append(int(sys.stdin.readline()))

for i in range(1, n+1):
    o = k // coin[-1*i]
    val += k // coin[-1*i]
    k = k - o * coin[-1*i]

print(val)
