N = 4
M = 5
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if graph[x][y] == 0:
        graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < M and nx >= 0 and ny >= 0 and graph[nx][ny] == 0:
            dfs(nx, ny)


result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)
