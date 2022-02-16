import math
from re import A
from turtle import distance

x = [1, 2, 6, 8]
y = [1, 2, 5, 7]


def solution(x, y):
    arrXY = make_graph(x, y)
    answer = 0
    for i in range(1, len(arrXY)):
        dx, dy = arrXY[i-1]
        nx, ny = arrXY[i]
        answer = max(answer, calulate_distance(nx - dx, ny - dy))

    return answer


def calulate_distance(n, k):
    result = (n**2 + k**2)**(1/2)

    return math.ceil(result)


def make_graph(x, y):
    arr = []
    for i in range(len(x)):
        arr.append((x[i], y[i]))
    arr.sort()
    return arr


solution(x, y)
