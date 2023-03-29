from itertools import combinations
def solution(numbers):
    result = combinations(numbers, 2)
    answer = []
    for k in result:
        hap = k[0] + k[1]
        if hap not in answer: answer.append(hap)
    answer.sort()
    return answer
