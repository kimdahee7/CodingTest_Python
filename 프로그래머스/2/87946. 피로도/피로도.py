from itertools import permutations
def solution(k, dungeons):
    answer = -1
    result = set()
    l = permutations(dungeons,len(dungeons))
    for i in l:
        total = 0
        k2 = k
        for j in i:
            if k2 >= j[0]:
                k2 -= j[1]
                total +=1
            else:
                break
        result.add(total)
    return max(result)