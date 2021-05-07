N,M = map(int,input().split())

arr = []
arr_correct_B = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]*4
arr_correct_W = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]*4

for i in range(N):
    line = input()
    arr.append(list(line))

minimum = 2501

for j in range(N-7):
    for k in range(M-7):
        arr_new = [row[k:k+8] for row in arr[j:j+8]]
        total_B = 0
        total_M = 0
        
        for l in range(8):
            for m in range(8):
                if arr_new[l][m] != arr_correct_B[l][m]:
                    total_B+=1

        for n in range(8):
            for o in range(8):
                if arr_new[n][o] != arr_correct_W[n][o]:
                    total_M+=1
                    
        if min(total_B,total_M)<=minimum:
            minimum = min(total_B,total_M)
            
print(minimum)