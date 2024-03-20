from collections import deque

def solution(queue1, queue2):
    queue = deque()
    total = sum(queue1) + sum(queue2)
    target = total // 2
    queue.append((queue1, queue2, 0))
    visit_list = []
    while queue:
        q1, q2, i = queue.popleft()
        visit_check = 'A'
        for a in q1:
            visit_check += str(a)
        visit_check += 'B'
        for b in q1:
            visit_check += str(b)
        if visit_check in visit_list:
            continue
        visit_list.append(visit_check)
        
        if sum(q1) == target:
            return i
        
        
        if q1:
            tmpq1 = q1[:]
            tmpq2 = q2[:]
            tmp1 = tmpq1.pop(0)
            tmpq2.append(tmp1)
            queue.append((tmpq1, tmpq2, i+1))
        if q2:
            tmpq1 = q1[:]
            tmpq2 = q2[:]
            tmp2 = tmpq2.pop(0)
            tmpq1.append(tmp2)
            queue.append((tmpq1, tmpq2, i+1))

    return -1

#bfs로 풀어보려했는데 시간초과