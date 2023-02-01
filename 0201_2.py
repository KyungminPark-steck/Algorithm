# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:31:00 2023

@author: 82102
"""

def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if answer == []: answer = [-1] 
    else: answer.sort()
    return answer

