import sys
N = int(sys.stdin.readline().rstrip())
graph = []
visit = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def solution(x,y):
    stack = []
    answer = 1
    visit[x][y] = 1
    stack.append((x,y))
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if graph[nx][ny] == '1' and visit[nx][ny] == 0:
                    answer +=1
                    visit[nx][ny] = 1
                    stack.append((nx,ny))
    return answer

arr = []
tot = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and graph[i][j] == '1':
            arr.append(solution(i,j))
            tot +=1
print(tot)
for i in sorted(arr):
    print(i)