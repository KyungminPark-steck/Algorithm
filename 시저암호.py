def solution(s, n):
    answer = list(s)
    for i in range(len(answer)):
        if answer[i] == ' ': continue
        c = ord('A') if answer[i].isupper() else ord('a')
        answer[i] = chr((ord(answer[i]) - c + n) % 26 + c)

    return ''.join(answer)
