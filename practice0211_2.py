from collections import deque
N = 5
M = 6
graph = [[1, 0, 1, 0, 1, 0, ], [1, 1, 1, 1, 1, 1], [
    0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y] + graph[nx][ny]
                    queue.append((nx, ny))
    return visit[N-1][M-1]


print(bfs(0, 0))
