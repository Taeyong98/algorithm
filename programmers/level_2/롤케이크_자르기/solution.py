def solution(topping):
    answer = 0
    topping_num = len(topping)
    forward_list =[0]*topping_num
    forward_set = set()
    forward_count = 0
    backward_list = [0]*topping_num
    backward_set = set()
    backward_count = 0
    for i in range(topping_num):
        if topping[i] not in forward_set:
            forward_count += 1
            forward_set.add(topping[i])
        forward_list[i] = forward_count
    
    for i in range(topping_num-1, -1, -1):
        if topping[i] not in backward_set:
            backward_count += 1
            backward_set.add(topping[i])
        backward_list[i] = backward_count
            
    for i in range(topping_num-1):
        if backward_list[i+1] == forward_list[i]:
            answer+=1
    
    
    return answer

#누적합 느낌으로 풀 수 있어요. O(n^2)가 브루트포스라면 O(n)으로 가능 정확히는 O(3*n)