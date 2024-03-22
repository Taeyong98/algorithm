lang_list = ["cpp", "java", "python"]
pos_list = ["backend", "frontend"]
j_s_list = ["junior", "senior"]
soulfood_list = ["chicken", "pizza"]

def solution(info, query):
    answer = []
    
    lang_dict = {a : set() for a in lang_list}
    pos_dict = {a : set() for a in pos_list}
    j_s_dict = {a : set() for a in j_s_list}
    soulfood_dict = {a : set() for a in soulfood_list}
    all_set = set()
    
    for i, info_string in enumerate(info):
        lang, pos, j_s, soulfood, score = info_string.split(" ")
        score = int(score)
        lang_dict[lang].add((score, i))
        pos_dict[pos].add((score, i))
        j_s_dict[j_s].add((score, i))
        soulfood_dict[soulfood].add((score, i))
        all_set.add((score, i))
        
    
    for qry in query:
        _set = set()
        qry = qry.replace("and ", "")
        lang, pos, j_s, soulfood, score = qry.split(" ")
        score = int(score)
        if lang == '-' and pos == '-' and j_s == '-' and soulfood == '-':
            _set = _set.union(all_set)
        else:
            if lang != '-':
                _set = _set.union(lang_dict[lang])
            if pos != '-':
                if _set:
                    _set = _set.intersection(pos_dict[pos])
                else :
                    _set = _set.union(pos_dict[pos])
            if j_s != '-':
                if _set:
                    _set = _set.intersection(j_s_dict[j_s])
                else:
                    _set = _set.union(j_s_dict[j_s])
            if soulfood != '-':
                if _set:
                    _set = _set.intersection(soulfood_dict[soulfood])
                else:
                    _set = _set.union(soulfood_dict[soulfood])
        count = 0
        for a in _set:
            if a[0] >= score:
                count += 1
        answer.append(count)
    
    return answer

# set을 이용하여 풀려고 했으나 시간초과