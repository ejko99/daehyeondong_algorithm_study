import sys

stack = []

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
