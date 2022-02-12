from collections import deque
N = 5
M = 6
graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [
    0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < N and ny < M and nx >= 0 and ny >= 0:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[nx][ny] + graph[x][y]
                    queue.append((nx, ny))
    return print(graph[N-1][M-1])


bfs(0, 0)
