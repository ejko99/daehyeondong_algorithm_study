import sys
import collections

N, K = map(int, sys.stdin.readline().split())
q = collections.deque([x+1 for x in range(N)])
l = []

while len(q) != 0:
    q.rotate(-(K % len(q)))
    l.append(q.pop())

print('<'+', '.join(map(str, l))+'>')
