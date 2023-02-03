# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:58:48 2023

@author: 82102
"""

def solution(n, m):
    answer = []
    
    n_list, m_list = [], []
    for i in range(1,n+1):
        if n % i == 0:
            n_list.append(i)
    for j in range(1, m+1):
        if m % j == 0:
            m_list.append(j)
    li = list(set(n_list) & set(m_list))
    
    answer.append(max(li))
    
    k = m * n 
    b_n, b_m = [], []
    for i in range(1, k+1):
        b_n.append(n*i)
        b_m.append(m*i)
    
    lis = list(set(b_n) & set(b_m))
    answer.append(min(lis))
    
    return answer
