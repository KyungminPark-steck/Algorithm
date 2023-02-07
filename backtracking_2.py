a = int(input())

answer = []
check = [False] * (a+1)

def print_answer():
    for elem in answer:
        print(elem, end = ' ')
    print()


def choose(current_num):

    if current_num == a:
        print_answer()
    
    

    for i in range(1, a+1):
        if check[i]:
            continue
            
n, m = list(map(int, input().split()))


answer = []

def print_answer(answer):
    for elem in answer:
        print(elem, end = ' ')
    print()

def choose(current_num, cnt):
    if current_num == n+1:
        if cnt == m:
            print_answer(answer)
        return 
    
    answer.append(current_num)
    choose(current_num+1, cnt+1)
    answer.pop()

    choose(current_num+1, cnt)

    return 

choose(1,0)

k, n = list(map(int, input().split()))
#1부터 k 를 이용해서, n자리 숫자. 

answer = []
def print_answer(answer):
    for elem in answer:
        print(elem, end = ' ')
    print()

def choose(current_num):
    if current_num == n+1:
        print_answer(answer)
        return 
    for i in range(1, k+1):    
        if len(answer) >= 2 and answer[-1] == i and answer[-2] == i:
            continue
        answer.append(i)
        choose(current_num+1)
        answer.pop()
    return 


choose(1)
