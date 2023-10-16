def solution(arr):
    answer = []
    start = -1
    for i in arr:
        if i != start:
            answer.append(i)
            start = i
    return answer