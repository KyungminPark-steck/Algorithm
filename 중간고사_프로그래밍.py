# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:18:01 2022

@author: 82102
"""

my_day = "My day First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple. I play outside. I like to play. I read a book. I like to read books. I walk home. I do not like walking home. My mother cooks soup for dinner. The soup is hot. Then, I go to bed. I do not like to go to bed."

print("\n ### 1. 위 데이터의 단어 목록을 정리하고, 내림차순으로 정렬하여 출력하기 ### \n")
myday_low = my_day.lower()
myday_del = myday_low.replace(",", "").replace(".",'')
myday_list1 = myday_del.split()
myday_real = set(myday_list1)   #최종 집합
myday_list2 = list(myday_real) #최종 리스트
myday_list3 = list(myday_real)  #2랑 같은 거 하나 더

print("\n ### 1-1 sort 를 활용한 내림차순 ### \n")
myday_list2.sort(reverse = True)
print(myday_list2)
print("\n ### 1-2 sorted 를 활용한 내림차순 ### \n")
print(sorted(myday_list2, reverse = True))
print("\n ### 1-3 슬라이싱을 활용한 내림차순 ### \n")
myday_list3.sort()
print(myday_list3[::-1])


print("\n ### 2. 위 데이터의 단어 목록을 오름차순 정렬한 것을 홀수 번쨰의 단어들만 출력하기 ### \n")
my_day = "My day First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple. I play outside. I like to play. I read a book. I like to read books. I walk home. I do not like walking home. My mother cooks soup for dinner. The soup is hot. Then, I go to bed. I do not like to go to bed."

myday_low = my_day.lower()
myday_del = myday_low.replace(",", "").replace(".",'')
myday_list1 = myday_del.split()
myday_real = set(myday_list1)   
myday_list2 = list(myday_real) 
myday_list3 = list(myday_real)  
myday_list3.sort() #myday_list3 

i = 0
for i in range(len(myday_list3)):
    if i%2 == 0:
        print(myday_list3[i], end = ' ')
        i = i+1

print("\n ### 3. 위 문장을 문장부호를 삭제하지 말고 포함한 상태로 나누어 리스트를 자료형으로 만들고 출력하기 ### \n")
my_day = "My day First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple. I play outside. I like to play. I read a book. I like to read books. I walk home. I do not like walking home. My mother cooks soup for dinner. The soup is hot. Then, I go to bed. I do not like to go to bed."
my_day_replace = my_day.replace('\.', '\. ').replace('\,', '\, ')
my_day_split = my_day_replace.split()

word_split = []

for i in my_day_split:
    if ',' in i:
        a = len(i)
        word_split.append(i[:a-1])
        word_split.append(i[a-1])
    elif '.' in i:
        a = len(i)
        word_split.append(i[:a-1])
        word_split.append(i[a-1])
    else:
        word_split.append(i)

print(word_split)


print("\n ### 4. 일부 단어만 추출 ### \n")
my_day = "My day First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple. I play outside. I like to play. I read a book. I like to read books. I walk home. I do not like walking home. My mother cooks soup for dinner. The soup is hot. Then, I go to bed. I do not like to go to bed."


myday_low = my_day.lower()
myday_del = myday_low.replace(",", "").replace(".",'')
myday_list1 = myday_del.split()
myday_real = set(myday_list1)   
myday_list2 = list(myday_real) 
myday_list3 = list(myday_real)  
content_word_1 = []
content_word_2 = []
content_word_3 = []
content_word_4 = []

print("\n ### 4-1. 인칭대명사만 제외 ### \n") 
i = 0
for i in range(len(myday_list3)):
    if myday_list3[i] not in ["i", "my",]:
        content_word_1.append(myday_list3[i])
        i = i+1
    else:
        i = i+1
print(content_word_1)
print(len(content_word_1))

print("\n ### 4-2 be, 조동사만 제외 ### \n")
i = 0
for i in range(len(myday_list3)):
    if myday_list3[i] not in ["is","do"]:
        content_word_2.append(myday_list3[i])
        i = i+1
    else:
        i = i+1
print(content_word_2)
print(len(content_word_2))

print("\n ### 4-3. a, an, the 제외 ### \n")
i = 0
for i in range(len(myday_list3)):
    if myday_list3[i] not in ["a", "an", "the"]:
        content_word_3.append(myday_list3[i])
        i = i+1
    else:
        i = i+1
print(content_word_3)
print(len(content_word_3))

print("\n ### 4-4. 모두 제외  ### \n")
i = 0
for i in range(len(myday_list3)):
    if myday_list3[i] not in ["i", "my","is","do", "a", "an", "the"]:
        content_word_4.append(myday_list3[i])
        i = i+1
    else:
        i = i+1
print(content_word_4)
print(len(content_word_4))


print("\n ###  5. 목소리의 높낮이 정보 데이터에서 추출 ### \n")
subject_pitch = ["James", 144, "Mike", 147, "Oliver", 148, "Mary", 172, "Susie", 170, "Anthony", 133, "Tom", 141, "Peter", 144,
"Harry", 130, "Dennis", 146, "Fred", 148, "Jim", 152, "Noah", 149, "William", 143, "Mason", 138, "Olivia", 165, "Henry", 143,
"Liam", 142, "George", 155, "Andrew", 135, "Frank", 144]

print("\n ###  5-1.슬라이싱 방법으로 pitch 와 name, 평균 ### \n")
i = 0
name = []
pitch = []
for i in range(len(subject_pitch)):
    if i%2 == 0:
        name.append(subject_pitch[i])
        i = i+1
    else:
        pitch.append(subject_pitch[i])
        result =sum(pitch)
        i = i+1
print(name)
print(pitch)
print(result/len(pitch))

print("\n ###  5-2. While 반복문 방법으로 pitch 와 name, 평균 ### \n")
name = []
pitch = [] 
i = 0
while True:
    if i%2 == 0:
        name.append(subject_pitch[i])
        i = i+1
    else:
        pitch.append(subject_pitch[i])
        result2 =sum(pitch)
        i = i+1
    if i == len(subject_pitch):
        break
print(name)
print(pitch)
print(result2/len(pitch))

print("\n ### 5-3. 이름을 입력하면 입력 받은 이름과 그에 해당하는 pitch를 “The voice pitch of OOO is OOO, which is below/above average” 라고 출력하고, 만약 없는 이름을 입력하게 되면 ＂The name you entered is not found'이라고 출력하기  ### \n")
inname = input("Write down your name: ")
if inname in name:
    inpitch_index = name.index(inname)
    inpitch = pitch[inpitch_index]
    if inpitch > result2/len(pitch):
        print("The voice pitch of {} is {}, which is above average".format(inname, inpitch)) 
    else:
        print("The voice pitch of {} is {}, which is below average".format(inname, inpitch))
else:  
    print("The name you entered is not found")    


print(" ### \n 6. data 변수에서 prefix “un”이 포함된 단어만 추출하여 pre_un이라는 새로운 리스트에 담고 출력하기 ### \n")
dic = ['able', 'best', 'car', 'do', 'eat', 'fortunate', 'gun', 'hat', 'hungry', 'sunset', 'understand', 'usual']
data = ['best', 'car', 'eat', 'fortunate', 'gun', 'hat', 'hungily', 'hungry', 'sunset', 'unable', 'understading', 'undo', 'unfortunate', 'unusual']

i = 0
pre_un = []
for i in range(len(data)):
    if data[i] in dic:
        i = i+1
    else:
        if data[i][2:] in dic:
            pre_un.append(data[i])
            i = i+1
        else:
            i = i+1
print(pre_un)



my_day = "My day First, I wake up. Then, I get dressed. I walk to school. I do not ride a bike. I do not ride the bus. I like to go to school. It rains. I do not like rain. I eat lunch. I eat a sandwich and an apple. I play outside. I like to play. I read a book. I like to read books. I walk home. I do not like walking home. My mother cooks soup for dinner. The soup is hot. Then, I go to bed. I do not like to go to bed."
myday_low = my_day.lower()
myday_del = myday_low.replace(",", "").replace(".",'')
myday_list1 = myday_del.split()


print('\n ### 7. set 함수 사용하지 않고 중복제거 후, 오름차순 정렬하여 출력하기 ### \n')

unique_word = []
for i in myday_list1:
    if i not in unique_word:
        unique_word.append(i)

print(sorted(unique_word))



print('\n ### 8. 단어와 빈도를 딕셔너리에 담고 빈도를 기준으로 정렬하여 딕셔너리 출력, 상위 빈도 5개 단어 출력')

freq = {}

for i in range(len(unique_word)):
    freq[unique_word[i]] = myday_list1.count(unique_word[i])

a = sorted(freq.items(), key=lambda x: x[1], reverse = True) 
print(freq) 
print(a[0:5])
