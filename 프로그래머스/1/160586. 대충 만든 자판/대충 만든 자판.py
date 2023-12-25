def solution(keymap, targets):
    answer = []
    dic = {}
    for i in keymap:
        for j in range(len(i)):
            if i[j] in dic:
                dic[i[j]] = min(dic[i[j]],j+1)
            else:
                dic[i[j]] = j+1
    for i in targets:
        total = 0
        for j in i:
            if j in dic:
                total += dic[j]
            else:
                total = -1
                break
        answer.append(total)
    return answer