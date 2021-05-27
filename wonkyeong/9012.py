import sys

num = int(sys.stdin.readline())
stack = []

for i in range(num):
    point = 0
    count = 0
    x = sys.stdin.readline().rstrip()
    for j in range(len(x)):
        if x[j] == '(':
            stack.append(x[j])
            point += 1
        else:
            if point == 0:
                print('NO')
                count += 1
                break
            else:
                stack.pop()
                point -= 1
                
    if count == 0:
        print('YES') if point == 0 else print('NO')
