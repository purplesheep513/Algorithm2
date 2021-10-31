import sys
def solution(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

arr=[]
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

solution(arr)
for i in arr:
    print(i)