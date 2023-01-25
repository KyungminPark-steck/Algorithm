# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:33:36 2023

@author: 82102
"""

def solution(n):
    answer = 0
    while (n > 10):
        one = n % 10
        answer += one
        n = n // 10 
    answer += n
    return answer

solution(123)
solution(987)