def solution(n, m):
    answer = []
    for i in range(n, m+1):
        if compareStr(str(i)) != '':
            answer.append(compareStr(str(i)))
    return print(len(answer))


def compareStr(str):
    evenNum = 0
    if len(str) % 2 == 0:
        evenNum = 1
    else:
        evenNum = 0
    if str[0: len(str)//2] == str[len(str): (len(str)//2)-evenNum: -1]:
        return str
    else:
        return ''


solution(1, 5)
