import sys

size, num = map(int, sys.stdin.readline().rsplit())
card = list(map(int, sys.stdin.readline().split()))
sum = 0

for i in range(size-2):
    for j in range(i+1, size-1):
        for k in range(j+1, size):
            if (card[i]+card[j]+card[k] <= num) and (sum < card[i]+card[j]+card[k]):
                sum = card[i]+card[j]+card[k]
print(sum)
