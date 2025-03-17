def solution(arr):
    answer = [arr[0]]
    for a in range(1,len(arr)):
        if arr[a] != answer[-1]:
            answer.append(arr[a])
        else:
            continue
    return answer