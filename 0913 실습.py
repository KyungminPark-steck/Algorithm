# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:05:52 2022

@author: 82102
"""

''' ### 실습 1
def hap1():
    num1 = int(input("첫 숫자 입력: ")) #flaot 로 받고 넣을 수 있음 고려.
    
    num2 = int(input("두번째 숫자 입력: ")) #숫자를 안넣고 문자를 넣을 시 '예외처리'
    
    hap = num1 + num2 
    print('두 숫자의 합은',hap)
    
def hap2():
    num = input('한 번에 두 숫자 입력 받기, 스페이스로 구분: ')
    Num1 = int(num[0])
    Num2 = int(num[2])
    Hap = Num1 + Num2
    print('연속된 두 숫자의 합은', Hap)
    
hap1()
hap2()

#map 을 이용하는 방법 
a = map(int, a) #a라는 리스트에 존재하는 모든 인자에 앞의 것 int 적용, 새로운 변수에 할당 
print(sum, a)
'''

###실습 2
'''
def aletter_anal():
    aletter = input('enter the letter: ')
    
    if 'a' in aletter:
        print("THe word you enter includeds the letter 'a'")
        if aletter[0] == 'a':
            print("The word you enter starts with the letter 'a'")
        if aletter[-1] == 'a':
            print("The word you enter ends with the letter 'a'")
        ac = aletter.count('a')
        print("The words you enter includes %d 'a'", (ac))
    else:
        print("'a' not in the letter")
aletter_anal()
# word.starswith('a') / endswith 를 사용할 수도 있음.
'''
### 실습3
txt = '''Suppose that you could offer one word of advice to a young person living in the year 2000. One word! What would it be? Over the past few years, I have been asking this question of many friends, and the answers have been remarkably consistent. Three words are almost universally at the top of the list. The most frequently mentioned word is "Live." It is a sound choice for the First Maxim. If you have in mind Schweitzer's "reverence for life," and a biologist's sense of the complexity and wonder of the life process. you will understand the breadth and depth of the word.'''
data = txt.split()
u_txt = txt.upper()
l_txt = txt.lower()

data2= ""
for t in data:
    t = t.capitalize() #문자열의 첫 글자만 대문자로 만들어주는 capitalize.
    if data2 == "":
        data2 +=t
    else:
        data2 += ' '+t
print(data2)

u_data2 = txt.title() #문자열의 모든 단어에서 적용. 그러나 슈바이처 다음에 s가 대문자화. '다음을 첫 글자로 인식.
print(u_data2)




#글자수 세기 
include_c = print(len(txt)) #공백 포함 글자 개수
non_c = txt.replace(' ','') #뉴라인, 탭 감안하여 작성할 수 있음. ('/n','') ('/t','')
non_c = print(len(non_c)) #공백 미포함 글자 개수 
letter = set(txt)
print(len(letter)) #중복제거 글자 개수

count_list = []
for t in txt:
    if t not in count_list:
        count_list.append(t)

print(len(count_list)) #중복제거 글자 개수 ver2

#단어수 세기
txt1 = txt.replace('.','').replace('!','').replace('?','').replace(',','').replace('"','')
txt2 = txt.split()
print(len(txt2))
txt3 = set(txt2)
print(len(txt3)) #문장부호 제거 여부에 따라 중복제거 숫자는 다를 수 있음. 

dic = {}
for words in txt3:
    c = txt2.count(words)
    dic[words] = c

print(dic)

import operator
d = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print(d)

#대문자로 시작하는 단어 추출 
upper_list = []
for t in txt2:
    if t[0].isupper():
        upper_list.append(t)

print(upper_list)





