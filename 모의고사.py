def solution(answers):
    l_a = len(answers)
    supo_1, supo_2, supo_3 = [], [], []
    supo_1_li = [1,2,3,4,5]
    supo_2_li = [2,1,2,3,2,4,2,5]
    supo_3_li = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        supo_1.append(supo_1_li[i%5]) 
        supo_2.append(supo_2_li[i%8])
        supo_3.append(supo_3_li[i%10])
    

    dict = {'1': 0, '2':0, '3': 0}
    for i in range(l_a):
        if answers[i] == supo_1[i]: dict['1'] += 1
        if answers[i] == supo_2[i]: dict['2'] += 1 
        if answers[i] == supo_3[i]: dict['3'] += 1
    
    print(dict)
    
    answer = [int(k) for k,v in dict.items() if max(dict.values()) == v]
    
    return answer
