def solution(strings, n):
    for _ in range(len(strings)-1):
        for i in range(len(strings)-1):
            if ord(strings[i][n]) > ord(strings[i+1][n]): strings[i], strings[i+1] = strings[i+1], strings[i]
            elif ord(strings[i][n]) == ord(strings[i+1][n]): 
                strings[i:i+2] = sorted(strings[i:i+2])
    return strings
