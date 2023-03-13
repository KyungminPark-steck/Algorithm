def solution(n):
    gin_3 = []
    gin_10 = []
    
    while True:
        if n!=0:
            k = n%3 
            gin_3.append(k)
            n = n//3 
        else: break
    
    cnt = 0
    for i in gin_3[::-1]:
        print(i)
        key = i * (3**(cnt))
        gin_10.append(key)
        cnt += 1
    
    answer = sum(gin_10)
    return answer
