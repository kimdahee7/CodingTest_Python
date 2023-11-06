def solution(number, limit, power):
    answer = 0
    l = []
    for i in range(1,number+1):
        c = func(i)
        if c > limit:
            answer += power
        else:
            answer += c
    return answer


def func(i):
    total = 0
    for k in range(1,int(i**(1/2)) + 1):
        if i % k ==0:
            total +=1
            if (k**2) != i:
                   total +=1
    return total
    