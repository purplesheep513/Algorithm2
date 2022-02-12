N = 5
M = 3


def binary_search(array, target, start, end):
    result = False
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = True
            break
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return result


arr = [8, 3, 7, 9, 2]
search_arr = [3, 6, 10]
arr.sort()

for i in search_arr:
    if binary_search(arr, i, 0, N-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
