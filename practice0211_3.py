def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


N = 5
array = [8, 3, 7, 9, 2]
array.sort()
M = 3
x = [5, 7, 9]

for target in x:
    result = binary_search(array, target, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
