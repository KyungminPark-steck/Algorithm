def solution(rows, columns, queries):
    answer = []
    num_list = [[(i)*columns + (j+1) for j in range(columns)] for i in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1-1, y1-1, x2-1, y2-1, num_list))
    
    return result 
    
def rotate(x1, y1, x2, y2, num_list):
    min_val = num_list[x1][y1]
    first = num_list[x1][y1]
    for k in range(x1, x2):
        num_list[k][y1] = num_list[k+1][y1]
        min_val = min(min_val, num_list[k+1][y1])
    
    for k in range(y1, y2):
        num_list[x2][k] = num_list[x2][k+1]
        min_val = min(min_val, num_list[x2][k+1])
        
    for k in range(x2, x1, -1):
        num_list[k][y2] = num_list[k-1][y2]
        min_val = min(min_val, num_list[k-1][y2])
        
    for k in range(y2, y1+1, -1):
        num_list[x1][k] = num_list[x1][k-1]
        min_val = min(min_val, num_list[x1][k-1])
    
    num_list[x1][y1+1] = first
    return min_val 
