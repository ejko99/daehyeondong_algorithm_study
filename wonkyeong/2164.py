import sys

num = int(sys.stdin.readline())
q = [x+1 for x in range(num)]
front = 0
rear = num-1

while 1:
    if front == rear: break
    front += 2
    q.append(q[front-1])
    rear += 1

print(q[front])
