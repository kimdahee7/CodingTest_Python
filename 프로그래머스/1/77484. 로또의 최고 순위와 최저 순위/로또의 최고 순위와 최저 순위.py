def solution(lottos, win_nums):
    lotto = {}
    for i in lottos:
        if i not in lotto:
            lotto[i] = 1
        else:
            lotto[i] +=1
    for i in win_nums:
        if i not in lotto:
            lotto[i] = 1
        else:
            lotto[i] +=1

    match = 0
    if 0 in lotto:
        zero = lotto[0]
    else:
        zero = 0
        
    for l in lotto:
        if lotto[l] == 2 and l != 0:
            match +=1
    max_rank = zero + match
    min_rank = match
    return [rank(max_rank),rank(min_rank)]

def rank(total):
    if total == 6:
        return 1
    elif total == 5:
        return 2
    elif total == 4:
        return 3
    elif total == 3:
        return 4
    elif total == 2:
        return 5
    else:
        return 6