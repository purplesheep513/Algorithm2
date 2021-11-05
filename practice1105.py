import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))

def solution(arr):
    arr = sorted(arr)
    if (arr[0] + arr[1] + arr[2]) % 3 != 0:
        return 0
    while arr[0] != arr[1] and arr[0] != arr[2] and arr[1] != arr[2] :
        arr = sorted(arr)
        if arr[0] == arr[1] == arr[2] :
            return 1
        elif arr[0]==arr[1] or arr[0] == arr[2] or arr[1] == arr[2] :
            return 0
        else : 
            arr[0], arr[2] = calculate_values(arr[0], arr[2])
            arr =[arr[0],arr[1],arr[2]]
    if arr[0] == arr[1] == arr[2] :
        return 1
    elif arr[0]==arr[1] or arr[0] == arr[2] or arr[1] == arr[2] :
        return 0

def calculate_values(var1,var2):
    return (var1+var1, var2-var1)

print(solution(arr))