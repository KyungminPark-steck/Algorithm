def solution(citations):
    citations.sort()
    citations = citations[::-1]
    # 0 0 1 0 3 8 9 10 >> 10 9 8 4 1 0 0 0
    print(citations)
    for i in range(len(citations)):
        if citations[i]  <= i: 
            return i
        
    return len(citations)
    
