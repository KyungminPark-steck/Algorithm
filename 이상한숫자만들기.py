def solution(s):
    s = list(s)
    new = []
    cnt = 0
    for k in s:
        if k == ' ':
            cnt =  0
            new.append(k)
            continue
        if cnt%2 == 0: 
            new.append(k.upper())
        else: new.append(k.lower())
        cnt += 1
    
        
    return ''.join(new)
