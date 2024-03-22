#dp 문제인듯? bfs로도 풀릴듯?
from collections import deque
def solution(x, y, n):
    answer = 0
    queue = deque()       
    
    queue.append((x, 0))
    visit_set = set()
    
    while queue:
        a, m = queue.popleft()
        
        if a==y:
            return m
        
        if a+n <= y and a+n not in visit_set:
            queue.append((a+n, m+1))
            visit_set.add(a+n)
        if a*2 <= y and a*2 not in visit_set:
            queue.append((a*2, m+1))
            visit_set.add(a*2)
        if a*3 <= y and a*3 not in visit_set:    
            queue.append((a*3, m+1))
            visit_set.add(a*3)
    
    return -1

#bfs로 풀었는데 visit_list 를 리스트로 할 필요없고 set으로 해도됨.