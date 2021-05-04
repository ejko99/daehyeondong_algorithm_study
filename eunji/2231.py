num = int(input())
length = len(str(num))

for i in range(int(num/(10**3))*(10**3),num+1):
    total = i + sum(map(int,str(i)))
    if total == num:
        break

if i==num:
    print(0)
else:
    print(i)