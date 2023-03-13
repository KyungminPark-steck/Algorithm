def solution(s):
    iter, cnt_0 = 0, 0
    while s != '1':
        iter += 1 
        cnt_1 = s.count('1') # 3 
        cnt_0 += len(s) - cnt_1 
        s = bin(cnt_1)[2:] # 3 >> 1 1 >> 0 1 
    # "011"
    return [iter, cnt_0]
