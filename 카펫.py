def solution(brown, yellow):
    answer = []
    hap = brown + yellow # 10 + 2 = 12 
    yaksu = []
    for i in range(1, hap//2): # 1... 6까지
        if hap%i == 0: yaksu.append([hap//i, i]) # 12,1 / 6,2 / 4,3 / 
    
    print(yaksu)
    for y in yaksu:
        
        if yellow == (y[0]-2) * (y[1]-2): 
            answer = y 
            break
        
    return answer
