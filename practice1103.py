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

# 생각해보면 간단한것인데 나는 +인경우 -인경우 두가지를 동시에 어떻게 실행하느냐에 집착하고있었다.
# 그냥 계속 stack에 쌓고, 인덱스를 보내면 그 인덱스에 맞게 더해주므로 그렇게 생각하면 되는것이었다. 아직 멀었구나 난