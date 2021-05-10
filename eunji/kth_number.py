def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_new = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(array_new[commands[i][2]-1])
    return answer