direction = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (-1, 2), (1, -2), (-1, -2)]
matchingChar = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def solution(x):
    nx = int(x[1])
    ny = matchingChar[x[0]]
    result = 0
    for i in direction:
        dx = nx + i[0]
        dy = ny + i[1]
        if dx >= 1 and dy >= 1 and dx <= 8 and dy <= 8:
            result += 1
    print(result)


solution('c2')
