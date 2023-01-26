# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:43:53 2023

@author: 82102
"""

def solution(n):
    answer = []
    while (n > 10):
        one = n%10 
        answer.append(one)
        n = n//10
    answer.append(n)
    return answer