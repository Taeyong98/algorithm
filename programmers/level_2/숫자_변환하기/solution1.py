#dp 문제인듯? bfs로도 풀릴듯?
from collections import deque
def solution(x, y, n):
    answer = 0
    queue = deque()       
    
    queue.append((x, 0))
    visit_list = []
    
    while queue:
        a, m = queue.popleft()
        if a > y or a in visit_list:
            continue
        
        if a==y:
            return m
        
        queue.append((a+n, m+1))
        queue.append((a*2, m+1))
        queue.append((a*3, m+1))
    
    return -1
#bfs로 풀었을 때, 시간초과 남 DP ㄱㄱ
