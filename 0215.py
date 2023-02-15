def solution(n):
    answer = []
    for i in range(n+1):
        if i <= 1:
            answer.append(i)
        else:
            k = answer[i-1] + answer[i-2]
            answer.append(k % 1234567)
        
    return answer[-1]
