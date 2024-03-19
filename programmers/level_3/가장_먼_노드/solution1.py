from collections import deque

def solution(n, edge):
    answer = 0
    _map = [[0 for _ in range(n)] for _ in range(n)]
    
    for a,b in edge:
        _map[a-1][b-1] = 1
        _map[b-1][a-1] = 1
    
    visited = [0 for _ in range(n)]
    queue = deque()
    queue.append((0, 1))
    
    while queue:
        a, b = queue.popleft()
        if visited[a]:
            continue
        visited[a] = b
        
        for i in range(n):
            if _map[a][i] and not visited[i]:
                queue.append((i, b+1))
    
    m = max(visited)
    
    for visit in visited:
        if visit == m:
            answer+=1
    
    return answer

# BFS로 풀어보려 했으나 시간초과