# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:53:47 2023

@author: 82102
"""

a = int(input())

x, y = 0, 0
dx , dy = [1, 0, -1, 0], [0, -1, 0, 1]


for _ in range(a):
    dir, dis = tuple(input().split())
    dis = int(dis)

    if dir == "E":
        move_dir = 0
    elif dir == "W":
        move_dir = 2
    elif dir == 'N':
        move_dir = 3
    else:
        move_dir = 1
    # dir = N, dist = 3 
    x, y = x + dx[move_dir]*dis , y + dy[move_dir]*dis
   
print(x, y)


x, y = 0, 0
dir_num = 3
dx, dy =[1,0,-1,0], [0,-1, 0, 1]

commmands = input()

for cmd in commmands:
    if cmd == "L":
        dir_num = (dir_num+3) % 4 
    elif cmd == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num] , y + dy[dir_num]

print(x, y)

n = int(input())
a= []
for i in range(n):
    li = list(map(int, input().split()))
    a.append(li)

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy

            if in_range(nx, ny) and a[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1

print(result)

arr = list(map(int, input().split()))
n = arr[0] 
t = arr[1]

arr1 = input().split()
r = int(arr1[0]) -1
c = int(arr1[1]) -1 
d = arr1[2]

dxs , dys = [0, 1, -1, 0] , [1, 0, 0, -1]

def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < n 
mapping = {
    "R" : 0,
    "D" : 1,
    "U" : 2,
    "L" : 3
}


dir = mapping[d]
while True:
    nx, ny = r + dxs[dir], c + dys[dir]
    if not in_range(nx, ny):
        dir = 3 - dir
        t = t -1 
    else:
        r, c = r + dxs[dir], c + dys[dir]
        t = t -1 
    if t == 0:
        print(r+1, c+1)
        break
    
n = 4
answer = [
    [0] * n
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0           # 시작은 (0, 0) 입니다.
dir_num = 0           # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

# 처음 시작 위치에 초기값을 적습니다.
answer[x][y] = 1

# n*n번 진행합니다.
for i in range(2, n * n + 1):
    # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 더 이상 나아갈 수 없다면
    # 시계방향으로 90'를 회전합니다.
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

# 출력:
for i in range(n):
    for j in range(n):
        print(answer[i][j], end = ' ')
    print()
    
n = int(input())

x, y = 0, 0
dx, dy = [1,0,-1,0] , [0, -1, 0, 1]
mapping = {
    "N": 3,
    "E": 0,
    "W": 2,
    "S": 1
}
cnt = 0
a = ''
#for i in range(n):
for i in range(n):
    dir, dis = tuple(input().split())
    dis = int(dis)
    dir = mapping[dir]
    for _ in range(dis):
        x , y = x + dx[dir], y + dy[dir]
        cnt += 1
        if x==0 and y ==0:
            print(cnt)
            a = "now"
    if a == "now":
        break
if a =='':
    print(-1)
    
arr = input()

x, y = 0, 0
dx, dy = [1,0,-1,0] , [0, -1, 0, 1]
cnt = 0
dir = 3
for a in arr:
    if a == 'L':
        dir = (dir + 1) % 4 
        cnt += 1
    elif a == 'R': 
        dir = (dir + 3) % 4 
        cnt += 1
    else:
        x , y = x + dx[dir] , y + dy[dir]
        cnt+= 1
    if x == 0 and y ==0:
        print(cnt)
        break
    if len(arr) == cnt:
        print(-1)
        break

n, m = tuple(input().split())
n = int(n)
m = int(m)

arr = [
    [0] * n
    for _ in range(m)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, 1, 0, -1] , [1, 0, -1, 0]
for i in range(m):
    r, c = tuple(input().split())
    r = int(r) -1 
    c = int(c) -1 
    if in_range(r, c):
        arr[r][c] = 1
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx , c + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
        
    if cnt == 3:
        print(1)
    else:
        print(0)
        
n, t = tuple(input().split())
n = int(n)
t = int(t)

inp = input()

arr = []
for i in range(n):
    ar = list(map(int, input().split()))
    arr.append(ar)

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dx, dy = [0, 1, 0, -1] , [1, 0, -1, 0]
dir = 3
x = n // 2
y = n // 2 

hap = arr[x][y]
for k in inp:
    if k == "R":
        dir = (dir + 1) % 4 
    elif k == "L":
        dir = (dir + 3) % 4 
    else:
        # in range
        # x, y 
        nx, ny = x + dx[dir] , y + dy[dir]
        if in_range(nx, ny):
            x, y = x + dx[dir] , y + dy[dir]
            hap += arr[x][y]
print(hap)
해설의 코드