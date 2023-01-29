# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:29:15 2022

@author: 82102
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

dic2 = ['ad', 'aa', 'ah', 'ak', 'ac', 'al', 'ag', 'ai', 'ab', 'af', 'aj', 'ae']

print("result:", quick_sort(dic2))