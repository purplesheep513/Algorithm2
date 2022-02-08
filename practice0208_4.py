def solution(N, K):
    subnum = int(N % K)
    denum = N - subnum
    while True:
        if denum == 1:
            break
        denum = denum // K
        subnum += 1
    return int(subnum)


print(solution(17, 4))
