def solution(N, M, K):
    N.sort(reverse=True)
    first = N[0]
    second = N[1]
    cnt = 0
    result = 0
    for i in range(M):
        if cnt == K:
            cnt = 0
            result += second
            continue
        result += first
        cnt += 1
    return result


N = [3, 4, 3, 4, 3]
M = 7
K = 2
print(solution(N, M, K))
