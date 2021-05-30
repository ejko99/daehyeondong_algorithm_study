import sys

num = int(sys.stdin.readline())
q = []
front = 0
end = 0

for i in range(num):
    order = sys.stdin.readline().split()
    if order[0]=='push':
        q.append(int(order[1]))
        end += 1
    elif order[0]=='pop':
        if front==end:
            print(-1)
        else:
            print(q[front])
            front += 1
    elif order[0]=='size': print(end - front)
    elif order[0]=='empty': print(1) if front==end else print(0)
    elif order[0]=='front': print(-1) if front==end else print(q[front])
    else: print(-1) if front==end else print(q[end-1])
