# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:55:36 2022

@author: 82102
"""


import re

data1 = '''Good morning, Mr. Smith. How are you? I’m fine, thank you. How’s the weather outside? It’s rainy today.'''

p = re.compile(r"[A-Z][a-z]+\b")
m = p.findall(data1)
print(m)