from collections import deque
import traceback

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(board):
    answer = 0
    _map = [[1 for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
    start = []
    
    for i, a in enumerate(board):
        for j , m in enumerate(a):
            if m == 'D':
                _map[i+1][j+1] = 1
            elif m == 'R':
                start.append((i+1,j+1))
                _map[i+1][j+1] = 0
            elif m == 'G':
                _map[i+1][j+1] = 2
            else:
                _map[i+1][j+1] = 0
                
    queue = deque()
    a, b = start[0]
    queue.append((a,b,0))
    visit = [[0 for _ in range(len(board[0])+2)] for _ in range(len(board)+2)]
    
    while queue:
        a, b, idx = queue.popleft()
        print(a,b,idx)
        if visit[a][b]:
            continue
        if _map[a][b] == 2:
            return idx

        visit[a][b] = 1

        for i in range(4):
            new_a = a
            new_b = b
            while _map[new_a][new_b] != 1:
                new_a = new_a + dx[i]
                new_b = new_b + dy[i]

            if not visit[new_a - dx[i]][new_b - dy[i]]:
                queue.append((new_a - dx[i], new_b - dy[i], idx+1))

    return -1

#BFS로 풀었음