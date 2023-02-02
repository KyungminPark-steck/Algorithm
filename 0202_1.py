# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:31:00 2023

@author: 82102
"""

def solution(s):
    arr = list(map(int, s.split()))
    return "{} {}".format(min(arr), max(arr))