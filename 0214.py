def solution(n):
    answer = 0
    hap = 0
    
    for j in range(n):
        hap = 0
        for i in range(j+1, n+1):
                hap += i
                if hap == n:
                    answer += 1
                    break  
                elif hap > n:
                    break
    
    return answer
