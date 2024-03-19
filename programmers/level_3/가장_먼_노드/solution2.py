from collections import deque

def solution(n, edge):
    answer = 0
    _map = [[] for _ in range(n+1)]
    
    for a,b in edge:
        _map[a].append(b)
        _map[b].append(a)
    
    visited = [0 for _ in range(n+1)]
    queue = deque()
    queue.append((1, 1))
    
    while queue:
        a, b = queue.popleft()
        if visited[a]:
            continue
        visited[a] = b
        
        for i in _map[a]:
            if not visited[i]:
                queue.append((i, b+1))
    
    m = max(visited)
    
    for visit in visited:
        if visit == m:
            answer+=1
    
    return answer
#solution1과 같지만 인접행렬 -> 인접 인덱스로 바꾸어 진행