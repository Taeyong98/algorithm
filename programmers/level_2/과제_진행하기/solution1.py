from collections import deque
from functools import cmp_to_key

def compare(a, b):
    if a[1] > b[1]:
        return 1
    if a[1] == b[1]:
        return 0
    else:
        return -1
    
def solution(plans):
    answer = []
    plans.sort(key = cmp_to_key(compare))
    stack = deque()
    idx = 0
    now_time = 0
    left = 0
    
    for name, start, playtime in plans :
        h,m = start.split(":")
        start_time = int(h)*60 + int(m)

        
        if idx == 0:
            now_name = name
            now_time = start_time
            left = int(playtime)
            idx+=1
            continue
        
        
        
        if start_time < now_time + left:
            stack.append((now_name, left - (start_time - now_time)))
            now_time = start_time
            now_name = name
            left = int(playtime)
            
        elif start_time == now_time + left:
            answer.append(now_name)
            now_time = start_time
            now_name = name
            left = int(playtime)
        else:
            while stack and start_time > now_time + left:
                answer.append(now_name)
                now_time = now_time + left
                now_name, left = stack.pop()
            if start_time < now_time + left:
                stack.append((now_name, left - (start_time - now_time)))
                now_time = start_time
                now_name = name
                left = int(playtime)
            else:
                answer.append(now_name)
                now_time = start_time
                now_name = name
                left = int(playtime)
        if idx == len(plans)-1:
            answer.append(name)
        
        idx +=1
    while stack:
        a, b = stack.pop()
        answer.append(a)
    return answer

#스케쥴링 스택 큐네
#시간을 어떻게 확인할까?

#이건 다시풀어보자.. 너무 오래걸렷음