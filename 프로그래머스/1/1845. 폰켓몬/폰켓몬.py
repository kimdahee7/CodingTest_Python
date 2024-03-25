def solution(nums):
    answer = 0
    n = len(nums)//2
    l = set(nums)
    if len(l) >= n:
        answer = n
    else:
        answer = len(l)
    return answer
