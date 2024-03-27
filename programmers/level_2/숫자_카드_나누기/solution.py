from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    
    def find_gcd(list_a):
        gcd_ = list_a[0]
        for a in list_a:
            gcd_ = gcd(gcd_, a)
        return gcd_
    
    def find_(list_a, list_b):
        x = find_gcd(list_a)
        for i in range(x, 0, -1):
            for a in list_a:
                if a % i != 0:
                    break
            else:
                for b in list_b:
                    if b % i == 0:
                        break
                else:
                    return i
        
        return 0
    
    return max(find_(arrayA, arrayB), find_(arrayB, arrayA))

#최대공약수 찾고 1씩 감소시키며 확인