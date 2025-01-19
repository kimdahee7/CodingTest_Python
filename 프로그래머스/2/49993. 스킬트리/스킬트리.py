def solution(skill, skill_trees):
    answer = 0
    dic = {}
    for s in range(len(skill)):
        if skill[s] not in dic:
            dic[skill[s]] = s
    for tree in skill_trees:
        current = -1
        check = 0
        for i in tree:
            if i in dic:
                if current + 1 == dic[i]:
                    current = dic[i]
                else:
                    check = 1
                    break
        if check == 0:
            print(tree)
            answer +=1
    return answer