# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:31:40 2023

@author: 82102
"""

def solution(s):
    if len(s) % 2 !=0:
        return s[len(s) // 2]
    else: return s[len(s) // 2 -1] + s[len(s) // 2]