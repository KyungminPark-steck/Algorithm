# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 21:14:01 2023

@author: 82102
"""
def solution(x, n):
    answer = []
    num = x
    for i in range(n):
        answer.append(num)
        num += x
    return answer

print(solution(4,3))

