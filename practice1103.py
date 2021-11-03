def solution(numbers, target):
    answer = 0
    stack = []
    stack.append((numbers[0],0))
    stack.append((-numbers[0],0))
    while stack:
        sum,idx = stack.pop()
        if idx + 1 < len(numbers):
            stack.append((sum + numbers[idx+1],idx+1))
            stack.append((sum - numbers[idx+1],idx+1))
        else:
            if sum== target:
                answer+=1

    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
