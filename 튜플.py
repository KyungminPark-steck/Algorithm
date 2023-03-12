def solution(s):
    s = s[2:-2]
    s = s.split("},{")
    s = sorted(s, key = lambda x : len(x))
    
    answer = []
    cnt = 1
    for k in s:
        k = list(map(int, k.split(',')))
        if cnt == len(k):
            for key in k:
                if not key in answer:
                    answer.append(key)
        cnt += 1
                
            
    
    return answer
