def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    #이기면 1 지면 -1
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1,-1]:
                    continue
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
    for row in board:
        #자기자신과 싸울 수없으므로 하나임
        if row.count(0) == 1:
            answer += 1
    return answer

#플로이드-워샬 문제와 비슷한 결임... 생각하기까지 어려울 수 있음