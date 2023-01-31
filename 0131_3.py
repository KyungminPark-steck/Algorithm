# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:21:39 2023

@author: 82102
"""

def solution(a,b):
    
    if a <= b:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))

print(solution(3, 5))
    