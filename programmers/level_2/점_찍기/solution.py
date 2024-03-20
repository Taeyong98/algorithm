def solution(k, d):
    answer = 0
    max_num = (d//k)*k
    answer += (max_num)//k+1
    for i in range(k, d+1, k):
        while max_num**2 + i**2 > d**2:
            max_num -= k
        answer += (max_num)//k+1
        
    return answer

#어려웟음.. 수학적 이해도 필요