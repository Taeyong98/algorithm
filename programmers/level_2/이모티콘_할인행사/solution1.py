from collections import deque
from itertools import combinations

discount_list = [10, 20, 30 ,40]

def solution(users, emoticons):
    answer = []
    tmp = [0 for _ in range(len(emoticons))]
    discount_comb = []
    def dfs(tmp, d):
        if d == len(tmp):
            discount_comb.append(tmp[:])
            return
        for discount in discount_list:
            tmp[d] += discount
            dfs(tmp, d+1)
            tmp[d] -= discount
    dfs(tmp,0)
    answer_list = []
    
    for discount in discount_comb:
        s_count = 0
        e_count = 0
        for user in users:
            u_count = 0
            for i, emoticon in enumerate(emoticons):
                if user[0] <= discount[i]:
                    u_count += int(emoticon * (100-discount[i])/100)
            
            if u_count >= user[1]:
                s_count += 1
            else:
                e_count += u_count
        answer_list.append((s_count,e_count))

    a, b = max(answer_list)
        
    return [a,b]

#dfs로 조합만드는 법 연습하기 
#다시 풀어볼거임