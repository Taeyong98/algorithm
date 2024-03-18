from collections import deque

def solution(tickets):
    answer = []
    _dict = {}
    city_set = set()
    for a,b in tickets:
        if a in _dict.keys():
            _dict[a].append(b)
        else:
            _dict[a] = list()
            _dict[a].append(b)
        city_set.add(a)
        city_set.add(b)
    
    queue = deque()
    
    queue.append(("ICN", tickets, ["ICN"]))
    
    while queue:
        a, left_tickets, visit_list = queue.popleft()
        if len(left_tickets) == 0:
            answer.append(visit_list)
            continue
        for i, left_ticket in enumerate(left_tickets):
            if a == left_ticket[0]:
                new_visit_list = [j for j in visit_list]
                new_visit_list.append(left_ticket[1])
                new_left_tickets = [j for j in left_tickets]
                new_left_tickets.pop(i)
                queue.append((left_ticket[1], new_left_tickets, new_visit_list))

    answer.sort()
        
    return answer[0]