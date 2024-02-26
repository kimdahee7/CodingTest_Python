def solution(s):
    answer = []
    l = {}
    for i in range(len(s)):
        if s[i] not in l:
            answer.append(-1)
            l[s[i]] = i
        else:
            answer.append(i-l[s[i]])
            l[s[i]] = i
    return answer