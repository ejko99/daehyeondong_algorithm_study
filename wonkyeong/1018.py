import sys

N, M = map(int, (sys.stdin.readline().split()))
cnt = 0

for r in range(N):
    row = list(sys.stdin.readline().split()[0])
    print(row)
    for c in range(M):
        if r == 0:
            if row[0] == 'B':
                start0, start1 = 'B', 'W'
            else:
                start0, start1 = 'W', 'B'
        if (r % 2 == c % 2):
            if row[c] != start0:
                row[r][c] = start0
                cnt += 1
        else:
            if row[c] != start1:
                row[r][c] = start1
                cnt += 1
    print(row)

print(cnt)
