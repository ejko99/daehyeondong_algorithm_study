def solution(clothes):
    answer = 1
    dict = {}
    for i in range(len(clothes)):
        if clothes[i][1] in dict:
            dict[clothes[i][1]] = dict[clothes[i][1]] + 1
        else:
            dict[clothes[i][1]] = 1
    for value in dict.values():
        answer *= value+1
    
    return answer-1
