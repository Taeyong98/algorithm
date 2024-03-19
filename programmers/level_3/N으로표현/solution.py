from collections import deque

def solution(N, number):
    answer = 0
    dp = [ set() for _ in range (9)]
    for i in range(1,9):
        ans = ""
        for j in range(i):
            ans += f"{N}"
        dp[i].add(int(ans))
    
    for i in range(1,9):
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a*b)
                    dp[i].add(a-b)
                    dp[i].add(a+b)
                    try:
                        dp[i].add(a//b)
                    except:
                        pass
        if number in dp[i]:
            return i
    else:
        return -1    
    return answer

# DP 사용.. 어렵다