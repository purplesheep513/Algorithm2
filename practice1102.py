def solution(scoville, K):
    answer = 0
    answer = makeScoville(scoville, K,answer)
    return answer
    
def mixed(a,b):
    return a + b *2

def makeScoville(scoville, K,ans):
    while scoville[scoville.index(min(scoville))] < K:
        if len(scoville)<1:
            break
        ans +=1
        a = scoville.pop(scoville.index(min(scoville)))
        b = scoville.pop(scoville.index(min(scoville)))
        scoville.append(mixed(a,b))
    if scoville[scoville.index(min(scoville))] < K:
        ans = -1
    else : return ans
    return ans

scoville = [1,1,1,1,1,1,1,1,1,1,1, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))