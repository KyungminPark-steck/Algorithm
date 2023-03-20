
def solution(n):
    
    num_list = [[0]*i 
               for i in range(1, n+1)]
    
    dxs, dys = [1, 0, -1], [0, 1, -1]
    x, y = 0, 0
    dir_num = 0
    
    num_list[x][y] = 1

    for i in range(2, n*(n+1)//2 + 1):
        #일단 미리 갈 칸 계산
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        #해당 칸이 범위 내에 있지 않거나, 0이 아니라면 방향 전환  
        if in_range(nx, ny, n)==False or num_list[nx][ny] != 0:
            dir_num = (dir_num+1)%3 
        #방향에 따라 새롭게 계산
        x, y = x + dxs[dir_num], y + dys[dir_num]
        #할당 
        num_list[x][y] = i
        
    return [data for inner_list in num_list for data in inner_list]


def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y <= x
