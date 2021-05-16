import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    word = sys.stdin.readline().split()
    words.append((len(word), word))
    
words.sort(key=lambda x: x[0])

for i in range(n):
    print(words[i][1])
