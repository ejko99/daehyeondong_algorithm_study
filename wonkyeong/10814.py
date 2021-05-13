import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    l.append((int(age), name))
l.sort(key = lambda x: x[0])

for age, name in l:
    print(age, name)
