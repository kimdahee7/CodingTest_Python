from itertools import permutations
def solution(numbers):
    answer = 0
    per = []
    result = set()
    l = list(numbers)
    for i in range(1,len(l)+1):
        per += permutations(l,i)
    for j in per:
        result.add("".join(j))
    for a in result:
        k = 0 
        if a[0] != "0" and a != "1":
            for b in range(2,int(a)):
                if int(a)%b == 0:
                    k +=1
                    break
            if k == 0:
                answer +=1
    return answer