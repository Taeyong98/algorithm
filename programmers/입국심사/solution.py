def how_many_people(time, times):
    count = 0
    for slot in times:
        count += int(time/slot)
    return count

def solution(n, times):
    time = 1
    count = how_many_people(time,times)
    start = 1
    end = 2
    while count < n:
        start = time
        time = time * 2
        end = time
        count = how_many_people(time, times)
    
    while start < end:
        b = (start+end)//2 + 1
        if how_many_people(b,times) >= n:
            end = b
        else:
            start = b
            
    return b