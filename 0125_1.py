# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:06:46 2023

@author: 82102
"""

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i ==0:
            answer += i
    return answer

solution(5)
solution(12)