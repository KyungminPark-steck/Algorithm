# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:13:56 2023

@author: 82102
"""

def solution(s):
    answer = True
    s = s.lower()
    test = ('p' in s == False) & ('y' in s == False)
    if test == True:
        answer= True
    elif s.count('p') == s.count('y'):
        answer = True
    else: answer = False
    return answer

print(solution('americano'))
print(solution('Pyy'))
print(solution('pypY'))