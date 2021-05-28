def solution(brown, yellow):
    answer = [0,0] #width+2, height+2
    for h in range(1,2999):
        w = (brown-4)/2-h
        if h*w == yellow:
            answer[0] = max(h,w)+2
            answer[1] = min(h,w)+2
            break
    return answer
