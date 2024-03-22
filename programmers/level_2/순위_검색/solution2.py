from bisect import bisect_left, bisect_right

lang_list = ["cpp", "java", "python", "-"]
pos_list = ["backend", "frontend", "-"]
j_s_list = ["junior", "senior", "-"]
soulfood_list = ["chicken", "pizza", "-"]

query_list = [lang_list, pos_list, j_s_list, soulfood_list]

def get_name_list(lang, pos, s_j, soulfood):
    _list = list()
    key_list = [lang, pos, s_j, soulfood]
    def dfs(tmp, d):
        if d == 4:
            _list.append(tmp)
            return
        tmp1 = tmp
        dfs(tmp1 + key_list[d],d+1)
        dfs(tmp1 + "-",d+1)
    
    dfs("",0)
    
    return _list
        
            
def solution(info, query):
    answer = []
    key_list = []
    def dfs1(tmp, d):
        if d == 4:
            key_list.append(tmp)
            return
        tmp1 = tmp
        for a in query_list[d]:
            tmp1 = tmp
            tmp1 += a
            dfs1(tmp1, d+1)
            
    dfs1("",0)
    
    
            
    query_dict = {a:list() for a in key_list}
    
    for info_string in info:
        lang, pos, j_s, soulfood, score = info_string.split(" ")
        _list = get_name_list(lang,pos,j_s,soulfood)     
        for name in _list:
            query_dict[name].append(int(score))
        
        
    for key in query_dict.keys():
        query_dict[key].sort()
    
    for qry in query:
        _set = set()
        qry = qry.replace("and ", "")
        lang, pos, j_s, soulfood, score = qry.split(" ")
        left_idx = bisect_left(query_dict[lang+pos+j_s+soulfood],int(score))
        answer.append(len(query_dict[lang+pos+j_s+soulfood])-left_idx)
    
    return answer

#bisect << 이분탐색 dfs로 모든조합만들기 연습가능