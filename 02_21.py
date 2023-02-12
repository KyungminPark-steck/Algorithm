def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse= True)))
    
####

def solution(s):
    li = []
    for gwal in s:
        if gwal =='(':
            li.append(gwal)
        else:
            if len(li) == 0:
                return False
            elif li[-1] == '(':
                li.pop()
    if li != []:
        return False
    else: return True
