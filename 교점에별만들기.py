def solution(line):
    num_list, answer = [], []
    num_line = len(line) #4
    
    x_min = y_min = int(1e15) 
    x_max = y_max = -int(1e15)
    
    for i in range(num_line): 
        A, B, E = line[i]
        for j in range(i+1, num_line):
            C, D, F = line[j]
            if A*D == B*C:
                continue
            X = (B*F - E*D) / (A*D - B*C)
            Y = (E*C - A*F) / (A*D - B*C)
            if int(X) == X and int(Y) == Y:
                X = int(X)
                Y = int(Y)
                num_list.append([X, Y])
                if x_min > X : x_min = X
                if y_min > Y : y_min = Y
                if x_max < X : x_max = X
                if y_max < Y : y_max = Y 
                
        
    x_iter = x_max - x_min + 1
    y_iter = y_max - y_min + 1
    new_list = [['.']*x_iter for _ in range(y_iter)]
    
    for star_x, star_y in num_list:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        new_list[ny][nx] = '*'
                         
    for result in new_list:
        answer.append("".join(result))
    return answer[::-1]
    
                         
        
    
                    
