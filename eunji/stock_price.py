import collections

def solution(prices):
    deq = collections.deque(prices)
    answer=[]
    time=0
    for i in range(len(prices)):
        ele = deq.popleft()
        for j in range(i+1,len(prices)):
            if prices[j] < ele:
                time = j-i
                answer.append(time)
                # print(answer)
                break
            else:
                if j ==len(prices)-1:
                    time = j-i
                    answer.append(time)
                    # print(answer)
    answer.append(0)
    return answer