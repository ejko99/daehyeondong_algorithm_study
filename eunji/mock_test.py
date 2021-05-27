def solution(answers):
    answer = []
    first=0
    second=0
    third=0
    first_ans = [1,2,3,4,5] * (int(len(answers)/5)+1)
    second_ans = [2,1,2,3,2,4,2,5] * (int(len(answers)/8)+1)
    third_ans = [3,3,1,1,2,2,4,4,5,5] * (int(len(answers)/10)+1)
    for i in range(len(answers)):
        if first_ans[i]==answers[i]:
            first+=1
        if second_ans[i]==answers[i]:
            second+=1
        if third_ans[i]==answers[i]:
            third+=1
    arr = [first,second,third]
    max_value = max(arr)
    if first == max_value:
        answer.append(1)
    if second == max_value:
        answer.append(2)
    if third == max_value:
        answer.append(3)
    return answer
