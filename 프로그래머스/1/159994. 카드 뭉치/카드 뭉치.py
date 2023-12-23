def solution(cards1, cards2, goal):
    ind = -1
    for i in cards1:
        if i in goal and ind <= goal.index(i):
            ind = goal.index(i)
            goal.remove(i)
        elif i in goal and ind > goal.index(i):
            return "No"
        elif i not in goal:
            break
        else:
            continue
    ind = -1
    for i in cards2:
        if i in goal and ind <= goal.index(i):
            ind = goal.index(i)
            goal.remove(i)
        elif i in goal and ind > goal.index(i):
            return "No"
        elif i not in goal:
            break
        else:
            continue
    if len(goal) == 0:
        return "Yes"
    else:
        return "No"
        