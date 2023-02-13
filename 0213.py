def solution(s):
    global cnt 
    
    s = s.replace('0', '')
    len_s = len(s) 
    two_js = []
    while True:
        k = len_s % 2 
        two_js.append(k)
        len_s = len_s // 2 
        if len_s == 0:
            break 
    two_js = two_js[::-1]
    cnt += 1 
    return two_js

cnt = 0
zero_one = s.count('0')
A = []

while True:
    s = solution()
    if s =='1':
        zero_two = s.count('0')
        A.append(cnt)
        A.append(zero_one-zero_two)
        break 
