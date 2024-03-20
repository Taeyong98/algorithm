#오른쪽 아니면 아래로만 가면되네 그게 즉 최단거리임

def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    dp[0][0] = 1
    for a, b in puddles:
        dp[a-1][b-1] = -1
    
    for i in range(m):
        for j in range(n):
            if dp[i][j] == -1:
                continue
            if i != 0:
                if dp[i-1][j]!=-1:
                    dp[i][j] += dp[i-1][j]
                
            if j != 0:
                if dp[i][j-1]!=-1:
                    dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1] % 1000000007