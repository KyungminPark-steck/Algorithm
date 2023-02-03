# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:38:29 2023

@author: 82102
"""

a, b = map(int, input().strip().split(' '))

for _ in range(b):
    for _ in range(a):
        print("*", end = '')
    print()