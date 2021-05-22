def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    answer = ''
    flag = False
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            flag = True
            break
    if not flag:
        answer = participant.pop(-1)
        
    return answer
