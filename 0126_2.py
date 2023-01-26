# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:43:53 2023

@author: 82102
"""
def solution(n):
    root = n**(1/2)
    if root%1 ==0.0:
        answer = int((root+1)**2)
    else:
        answer = -1
    return answer


