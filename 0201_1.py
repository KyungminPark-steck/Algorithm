# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:22:50 2023

@author: 82102
"""

def solution(seoul):
    cnt = 0
    result = 0
    for s in seoul:
        cnt += 1
        if s == "Kim":
            result = cnt 
        answer = "김서방은 {}에 있다".format(result-1)
    return answer