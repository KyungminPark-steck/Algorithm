# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:07:29 2022

@author: 82102
"""


import re

data2 = '''Good morning, Mr. Smith. How are you? Mrs. Smith, good afternoon. How’s the weather outside? Good
night, Dr. Strange. What a beautiful day! Bye.'''

data = re.sub("[.?!] (?=[A-Z])", '  ', data2)


data= data.split('  ')
print(data)

