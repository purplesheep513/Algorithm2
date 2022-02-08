def solution(N, M, K):
    N.sort(reverse=True)
    first = N[0]
    second = N[1]

    cnt_1 = int(M / (K + 1)) * K + int(M % (K + 1))
    cnt_2 = M - cnt_1

    return first * cnt_1 + second * cnt_2


N = [2, 4, 5, 4, 6]
M = 8
K = 3
print(solution(N, M, K))
