def solution(arr):
    n = arr[0]
    for i in arr:
        if i < n:
            n = i
    arr.remove(n)
    if len(arr) == 0:
        return [-1]
    else:
        return arr