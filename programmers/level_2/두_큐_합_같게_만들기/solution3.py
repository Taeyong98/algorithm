from collections import deque

def solution(queue1, queue2):
    i = 0
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    
    if (q1_sum+q2_sum)%2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    limit = len(queue1)*4
    
    while True:
        if q1_sum == q2_sum:
            return i
        if q1_sum > q2_sum:
            tmp = queue1.popleft()
            q1_sum -= tmp
            q2_sum += tmp
            queue2.append(tmp)
        else:
            tmp = queue2.popleft()
            q1_sum += tmp
            q2_sum -= tmp
            queue1.append(tmp)
        i+=1
        if not queue1 or not queue2:
            return -1
        if i == limit:
            return -1
    

#sum 하는데 시간이 오래 소요되므로 그냥 곧장 계산해줬음.. Limit도 걸었음