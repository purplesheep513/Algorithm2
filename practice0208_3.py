def solution(Arr):
    result = min(Arr[0])
    for i in range(1, len(Arr)):
        result = max(min(Arr[i]), result)
    return result


Arr = [[7, 3, 1, 8], [3, 3, 3, 4]]
print(solution(Arr))
