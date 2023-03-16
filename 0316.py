#함수 선언할 때마다 0이 되면 안되므로 global 이용
global answer; answer= 0
def solution(num):
    global answer
    
    #500 이면 -1 
    if answer >= 500: answer = -1; return answer 
    # 1이면 바닥조건. 카운트 반환.
    if num == 1: return answer
    #그것도 아니라면 카운트 +1 증가시키고 짝수이면 나누고 홀수이면 *3+1 해줌.
    answer += 1
    solution(num//2) if num%2==0 else solution(num*3+1)

    return answer
  
def solution(n):
  return hanoi(n, 1, 3)


def hanoi(n, a, b):
    if n == 0 : return []
    return hanoi(n-1, a, (6-a-b)) + [[a,b]] + hanoi(n-1, (6-a-b), b)
profile
박경민
