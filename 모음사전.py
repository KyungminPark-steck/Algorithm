m_list = ['A', 'E', 'I', 'O', 'U']
a = []

def make_w_list(a, w, count): #a는 이전 문자열, w는 현재
    if count == 6: return 
    if w != '': a.append(w)
    for m in m_list:
        make_w_list(a, w+m, count+1)
        
def solution(word):
    make_w_list(a, '', 0)
    id = a.index(word)

    return id+1
