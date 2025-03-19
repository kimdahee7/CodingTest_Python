def solution(nums):
    answer = 0
    cnt = len(nums)//2
    kind = set(nums)
    if cnt <= len(kind):
        answer = cnt
    else:
        answer = len(kind)
    return answer