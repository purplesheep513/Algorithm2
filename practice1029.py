from collections import deque

def solution(p):
    answer = ''
    return answer

def isValanced(str):
    stack = []
    queue = deque()
    temp = ''
    for i in str:
        if i ==')':
            stack.append(i)
        else:
            queue.append(i)