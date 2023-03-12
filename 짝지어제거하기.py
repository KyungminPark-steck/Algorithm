def solution(s):
    answer = 0
    li = []
    for k in s:
        if len(li) == 0:
            li.append(k)
        elif li[-1] == k:
            li.pop()
            
        else: 
            li.append(k)
    
    sent = ''.join(li)
    if sent == '':
        answer = 1
    else : answer = 0
        

    return answer
