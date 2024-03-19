def solution(distance, rocks, n):

    rocks.append(0)
    rocks.append(distance)
    
    rocks.sort()
    rock_distance_list = [rocks[i+1] - rocks[i] for i in range(len(rocks)-1)]
    
    
    def rock_number(least_dist):
        count = 0
        distance = 0
        for i in range(len(rock_distance_list)):
            distance += rock_distance_list[i]
            if distance >= least_dist:
                distance = 0
            else:
                count+=1
        
        return count
    
    start = 1
    end = 1000000000
    
    while start <= end:
        b = (start+end)//2
        if rock_number(b) > n:
            end = b-1
        else:
            start = b+1
        
    return end