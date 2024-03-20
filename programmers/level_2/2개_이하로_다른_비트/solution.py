def solution(numbers):
    answer = []
    for number in numbers:
        i = 2
        while i <= number:
            if number%i >= i//2: #즉 1 이면
                i = i*2
            else:
                if i == 2:
                    answer.append(i//2+number)
                else:
    
                    answer.append(i//4+number)
                break
        if i > number:
            answer.append(number+i//2)

    return answer
#이것도 수학관련문제 .. 다시풀어보기