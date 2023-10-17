def solution(brown, yellow):
    answer = [0] *2
    l = func(yellow)
    for i in l[::-1]:
        if (i[0]+2)*2 + i[1]*2 == brown:
            answer = [i[0]+2,i[1]+2]
            break
    return answer

def func(yellow):
    t = ()
    result = []
    for i in range(1,yellow+1):
        if yellow%i == 0:
            t = (i,yellow//i)
            result.append(t)
    return result