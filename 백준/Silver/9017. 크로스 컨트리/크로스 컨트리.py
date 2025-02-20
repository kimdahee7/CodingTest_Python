from collections import defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    N_l = list(map(int,input().split()))
    dic_team = {}
    for i in N_l:
        if i not in dic_team:
            dic_team[i] = 1
        else:
            dic_team[i] += 1
    dic_score = defaultdict(list)
    score = 1
    for i in N_l:
        if dic_team[i] < 6:
            continue
        else:
            if i not in dic_score:
                dic_score[i] = [score]
            else:
                dic_score[i].append(score)
            score +=1
    for i in dic_score:
        dic_score[i].append(sum(dic_score[i][0:4]))
    result = []
    for i in dic_score:
        result.append((dic_score[i][-1],dic_score[i][4],i))
    result.sort(key=lambda x:(x[0],x[1]))
    print(result[0][-1])