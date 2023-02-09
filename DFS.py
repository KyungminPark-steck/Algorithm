n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [[0]*n for _ in range(n)]

#끊기지 않고 상, 하, 좌, 우 0이 아니면 연결된 것으로 파악. 

def in_range(x, y):
    return 0 <= x and x < n and 0 <=y and y < n

def can_go(x, y):
    return in_range(x, y) and visited[x][y] == 0 and arr[x][y] == 1

maeul_count = []
human_count = 0
def dfs(x, y):
    global human_count
    dxs, dys = [0,0,1,-1] , [1,-1,0,0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            human_count += 1 
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = 1
            human_count = 1

            dfs(i, j)

            maeul_count.append(human_count)
dfs(0,0)
visited[0][0] = 1

maeul_count.sort()

print(len(maeul_count))

for mc in maeul_count:
    print(mc)
