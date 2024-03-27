from functools import cmp_to_key
def compare(a,b):
    if a[0].lower() > b[0].lower():
        return 1
    elif a[0].lower() == b[0].lower():
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            if a[2] > b[2]:
                return 1
            elif a[2] == b[2]:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
    
def solution(files):
    answer = []
    compare_list = []
    for i, file in enumerate(files):
        head_idx = 0
        for idx, letter in enumerate(file):
            length = len(file)

        head_idx = 0
        while head_idx < length:
            try:
                int(file[head_idx])
                break
            except:
                head_idx += 1

        number_idx = head_idx
        while number_idx < length:
            try:
                int(file[number_idx])
                number_idx += 1
            except:
                break

        head = file[:head_idx]
        number = file[head_idx:number_idx]
        
        compare_list.append([head,int(number),i])
    compare_list.sort(key = cmp_to_key(compare))
    answer = [ files[i[2]] for i in compare_list]
        
    return answer

#정렬문제.