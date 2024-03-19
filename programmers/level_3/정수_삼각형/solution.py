def solution(triangle):
    answer = 0
    dp = [[0 for _ in range(1,j+2)] for j in range(len(triangle))]
    for i, tri in enumerate(triangle):
        if i == 0:
            dp[0][0] = tri[0]
            continue
        for j, num in enumerate(tri):
            try:
                dp[i][j] = max(dp[i][j], num + dp[i-1][j])
            except:
                pass
            try:
                if j==0:
                    continue
                dp[i][j] = max(dp[i][j], num + dp[i-1][j-1])
            except:
                pass
    m = len(triangle)-1
    
    return max(dp[m])
    #dp를 사용해서 구현