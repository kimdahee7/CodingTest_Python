def solution(X, Y):
    answer = ''
    result = {}
    l = []
    for i in X:
        if i in result:
            result[i] += 1
        else:
            result[i] =1
    for i in Y:
        if i in result and result[i] != 0:
            l.append(i)
            result[i] -=1
    if len(l) == 0:
        return "-1"
    elif set(l) == {"0"}:
        return "0"
    else:
        l.sort(reverse=True)
    for i in l:
        answer += i
    return answer