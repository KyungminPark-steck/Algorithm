def solution(s):
    answer = 0
    
    key_list = []
    #s ='f09f9989x'; length=2; [s[i:i+length] for i in range(0, len(s), length)]
    cnt = 0; a = ''

    
    for length in range(len(s)//2, 0, -1):
        key = [s[i:i+length] for i in range(0, len(s), length)]
        key_list.append(key)
    
    for k in key_list:
        for i in range(len(k)-1):
            if k[i] == k[i+1]:
                cnt += 1
            elif k[i] != [k+1]:
