N = 5
K = 6
arr = [10, 15, 16, 17, 19]
arr.sort()
result = 0
start = 0
end = N-1

while start <= end:
    total = 0
    mid = (start + end) // 2
    result = arr[mid]

    for item in arr:
        if item > result:
            total += item - result

    if total < K:
        end = mid - 1
    else:
        start = mid + 1

print(result)
