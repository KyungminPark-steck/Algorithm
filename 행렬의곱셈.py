
def solution(arr1, arr2):
    arr1, arr2 = arr1, arr2
    m = len(arr1)
    n = len(arr2[0])
    result = [[0]*n for _ in range(m)]
    
    for i in range(m): # 0, 1, 2
        for j in range(n): # 0, 1
            for k in range(len(arr1[0])): # 0,1,2
                result[i][j] += arr1[i][k]*arr2[k][j]
    return result
        
