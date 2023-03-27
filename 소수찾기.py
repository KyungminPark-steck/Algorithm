from itertools import permutations

def solution(numbers):
    answer = 0
    num = []
    for i in range(1, len(numbers)+1): # 4C1, 4C2 에서 1, 2를 담당하는 i
        aw = list(permutations(numbers, i))

        for a in aw:
            k = ''
            for i in range(len(a)):
                k += a[i]
            k = k.lstrip('0')
            if k not in num and k!= '': num.append(k)
    print(num)
    
    sosu = []
    
    for n in num:
        k = is_prime_number(n)
        if k == True and n != '1': sosu.append(n)

    answer = len(sosu)
    print(sosu)
        

    return answer


import math

# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, int(math.sqrt(int(x))) + 1):
        if int(x) % i == 0:
            return False # 소수가 아님
    return True # 소수임
