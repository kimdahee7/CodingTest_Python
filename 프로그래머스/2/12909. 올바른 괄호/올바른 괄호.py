def solution(s):
    answer = True
    l = []
    for i in s:
        if i == ")":
            if len(l) !=0:
                l.pop(len(l)-1)
            else:
                l.append(i)
        else:
            l.append(i)
    if len(l) == 0:
        answer = True
    else:
        answer = False
    return answer