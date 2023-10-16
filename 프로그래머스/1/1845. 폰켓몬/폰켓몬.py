def solution(nums):
    answer = 0
    N = len(nums)//2
    l = (set(nums))
    answer = min(len(l),N)
    return answer