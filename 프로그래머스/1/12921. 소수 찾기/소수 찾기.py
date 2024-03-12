import math
def solution(n):
    answer = 1
    for i in range(3,n+1):
        c = 0
        for j in range(2,int(math.sqrt(i) + 1)):
            if i%j ==0:
                c +=1
                break
        if c ==0:
            answer+=1
    return answer
