from itertools import combinations
def solution(nums):
    l = list(combinations(nums,3))
    total = 0 
    for i in l:
        s = sum(list(i))
        if func(s) == 1:
            total +=1 
    return total

def func(s):
    for i in range(2,s):
        if s%i == 0:
            return 0
    return 1