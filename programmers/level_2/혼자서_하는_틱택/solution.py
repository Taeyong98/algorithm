def solution(board):
    answer = 0
    
    diagonal = [[0,0,1,1,2,2], [0,2,1,1,2,0]]
    
    _map = [[0 for _ in range(3)] for _ in range(3)]
    
    o_count = 0
    x_count = 0
    
    for i, line in enumerate(board):
        for j, check in enumerate(line):
            if check == 'O':
                _map[i][j] = 1
                o_count += 1
            elif check == 'X':
                _map[i][j] = 2
                x_count += 1
            else:
                _map[i][j] = 0
                
    if x_count > o_count :
        return 0
    if o_count > x_count+1:
        return 0
    
    o_win = False
    x_win = False
    

    for a, b, c, d, e, f in diagonal:
        if _map[a][b] == 1 and _map[c][d] == 1 and _map[e][f] == 1:
            o_win = True
        if _map[a][b] == 2 and _map[c][d] == 2 and _map[e][f] == 2:
            x_win = True
    
    for i in range(3):
        for j in range(3):
            try:
                if _map[i][j] == 1 and _map[i][j+1] == 1 and _map[i][j+2] == 1:
                    o_win = True
            except:
                pass
            try:
                if _map[i][j] == 1 and _map[i+1][j] == 1 and _map[i+2][j] == 1:
                    o_win = True
            except:
                pass
            try:
                if _map[i][j] == 1 and _map[i+1][j+1] == 1 and _map[i+2][j+2] ==1:
                    o_win = True
            except:
                pass
            try:
                if _map[i][j] == 2 and _map[i][j+1] == 2 and _map[i][j+2] == 2:
                    x_win = True
            except:
                pass
            try:
                if _map[i][j] == 2 and _map[i+1][j] == 2 and _map[i+2][j] == 2:
                    x_win = True
            except:
                pass
            try:
                if _map[i][j] == 2 and _map[i+1][j+1] == 2 and _map[i+2][j+2] ==2:
                    x_win = True
            except:
                pass
        
    
    if o_win and x_win:
        return 0
    
    if o_win  and not x_win :
        if o_count == x_count+1:
            return 1
        else:
            return 0
    
    if not o_win and x_win:
        if o_count == x_count:
            return 1
        else:
            return 0
    
    return 1
