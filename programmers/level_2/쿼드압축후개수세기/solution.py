"""
0~2n
dp로 풀수 있을듯
"""

def solution(arr):
    answer = []
    n = len(arr)//2
    dp = []
    dp.append(arr[:])
    while n != 0:
        dp.append([[0 for _ in range(n)]for _ in range(n)])
        n = n//2
        
    zero_count = 0
    one_count = 0
    
    for dp_i in range(len(dp)-1):
        n = len(dp[dp_i])
        for i in range(0,n,2):
            for j in range(0,n,2):
                if dp[dp_i][i][j] == 1 and dp[dp_i][i+1][j] == 1 and dp[dp_i][i][j+1] == 1 and dp[dp_i][i+1][j+1] == 1:
                    dp[dp_i+1][i//2][j//2] = 1
                elif dp[dp_i][i][j] == 0 and dp[dp_i][i+1][j] == 0 and dp[dp_i][i][j+1] == 0 and dp[dp_i][i+1][j+1] == 0:
                    dp[dp_i+1][i//2][j//2] = 0
                else:
                    if dp[dp_i][i][j] == 1:
                        one_count += 1
                    elif dp[dp_i][i][j] == 0:
                        zero_count += 1
                        
                    if dp[dp_i][i+1][j] == 1:
                        one_count += 1
                    elif dp[dp_i][i+1][j] == 0:
                        zero_count += 1
                        
                    if dp[dp_i][i][j+1] == 1:
                        one_count += 1
                    elif dp[dp_i][i][j+1] == 0:
                        zero_count += 1
                        
                    if dp[dp_i][i+1][j+1] == 1:
                        one_count += 1
                    elif dp[dp_i][i+1][j+1] == 0:
                        zero_count += 1
                        
                    dp[dp_i+1][i//2][j//2] = -1
    
    if dp[-1][0][0]==1:
        return [0,1]
    elif dp[-1][0][0] == 0:
        return [1,0]

    return [zero_count, one_count]

#bottom up 으로 dp를 만들어 풀었음