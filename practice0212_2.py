from re import S
import re


N = 4
M = 5
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < N and ny < M and nx >= 0 and ny >= 0:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    stack.append((nx, ny))


result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)
