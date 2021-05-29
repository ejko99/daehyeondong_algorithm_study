import sys
import re

stack = []

while True:
    string = sys.stdin.readline().rstrip()
    if string == '.': break
    point = 0
    l = re.findall(r'[()[\]]', string)
    for i in l:
        if (i == '(') or (i == '['):
            stack.append(i)
            point += 1
        elif point == 0:
            point -= 1
            break
        elif i == ')':
            if stack.pop()=='(': point -= 1
            else: break
        else:
            if stack.pop()=='[': point -= 1
            else: break
                
    print('yes') if point == 0 else print('no')
