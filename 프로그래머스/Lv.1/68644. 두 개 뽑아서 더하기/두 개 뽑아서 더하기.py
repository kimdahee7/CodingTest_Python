from itertools import permutations
def solution(numbers):
    answer = set()
    l = permutations(numbers,2)
    for i in l:
        answer.add(i[0]+i[1])
    answer = list(answer)
    answer.sort()
    return answer