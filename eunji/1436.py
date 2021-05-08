import sys

input = sys.stdin.readline
N = int(input())

i = 665
arr = []

while(1):
    i += 1
    if '666' in str(i):
        arr.append(i)
    if len(arr) > 10000:
        break

print(arr[N-1])