# 캐릭터에게 필요한 요소 : 이동거리(1또는 -1)
# 칸에 필요한 요소 : 방문여부
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(N, M, X, Y, direction, space):
    distance = 1
    visit = [[0] * M for _ in range(N)]
    turnCount = 0
    while True:
        # 왼쪽으로 회전
        direction = (direction + 3) % 4

        if X + dx[direction] > 0 and X + dx[direction] < N and Y + dy[direction] > 0 and Y + dy[direction] < M:
            # 갈 곳이 바다도 아니고 방문도 안 한경우
            if space[X + dx[direction]][Y + dy[direction]] == 0 and visit[X + dx[direction]][Y + dy[direction]] == 0:
                X += dx[direction]
                Y += dy[direction]
                visit[X][Y] = 1
                distance += 1
                turnCount = 0
                continue
            else:
                turnCount += 1

            # 제자리 걸음 한 경우
            if turnCount == 4:
                if space[X - dx[direction]][Y - dy[direction]] == 0:
                    X -= dx[direction]
                    Y -= dy[direction]
                else:
                    break
    return distance


Arr = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
print(solution(4, 4, 1, 1, 0, Arr))
