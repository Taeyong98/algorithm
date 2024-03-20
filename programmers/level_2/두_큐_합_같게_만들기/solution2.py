from collections import deque

def solution(queue1, queue2):
    i = 0
    if sum(queue1)+sum(queue2)%2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while True:
        if sum(queue1) == sum(queue2):
            return i
        if sum(queue1) > sum(queue2):
            tmp = queue1.popleft()
            queue2.append(tmp)
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
        i+=1
        if not queue1 or not queue2:
            print(queue1)
            return -1
    
    return answer
#그리디로 풀어봤지만 시간초과