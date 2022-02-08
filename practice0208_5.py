direction = {'R': [1, 0], 'U': [0, -1], 'L': [-1, 0], 'D': [0, 1]}


def solution(N, Arr):
    result = [1, 1]

    for i in Arr:
        if result[0] + direction[i][1] > 1 and result[0] + direction[i][1] < N:
            result[0] += direction[i][1]
        if result[1] + direction[i][0] > 1 and result[1] + direction[i][0] < N:
            result[1] += direction[i][0]

    return result


N = 5
Arr = ['R', 'R', 'R', 'U', 'D', 'D']
print(solution(N, Arr))
