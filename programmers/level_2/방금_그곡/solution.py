def replace_chord(string):
    result = string.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a").replace("B#", 'b')
    return result

def solution(m, musicinfos):
    answer = []
    m = replace_chord(m)
    for musicinfo in musicinfos:
        # musicinfo = replace_chord(musicinfo)
        start,end,name,code = musicinfo.split(',')
        code = replace_chord(code)
        start_h, start_m = start.split(":")
        end_h, end_m = end.split(":")
        start = int(start_h) * 60 + int(start_m)
        end = int(end_h) * 60 + int(end_m)
        
        playtime = end-start
        
        play_code = ''
        for i in range(playtime):
            play_code +=code[i%len(code)]
        
        
        if m in play_code:
            answer.append((playtime,start*-1,name))
            
    if answer:
        return max(answer)[2]
    else : 
        return "(None)"
    
#kmp나 그런거 사용안하고 C#과 같은 코드를 c로 치환 후 풀이
