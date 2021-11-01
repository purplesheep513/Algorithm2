import sys
N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

def sortArray(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    lower_arr = sortArray(arr[:mid])
    higher_arr = sortArray(arr[mid:])

    merged_arr = []
    l = h =0
    while l < len(lower_arr) and h < len(higher_arr):
        if lower_arr[l] < higher_arr[h]:
            merged_arr.append(lower_arr[l])
            l += 1
        else :
            merged_arr.append(higher_arr[h])
            h += 1
    merged_arr += lower_arr[l:]
    merged_arr += higher_arr[h:]
    return merged_arr

arr = sortArray(arr)

for i in arr:
    print(i)