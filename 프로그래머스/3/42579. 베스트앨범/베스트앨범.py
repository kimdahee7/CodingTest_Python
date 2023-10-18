def solution(genres, plays):
    answer = []
    g_dic = {}
    p_dic = []
    for i in range(len(genres)):
        if genres[i] in g_dic:
            g_dic[genres[i]] += plays[i]
        else:
            g_dic[genres[i]] = plays[i]
    g_dic = sorted(g_dic,key=lambda x:g_dic[x],reverse=True)
    for i, val in enumerate(plays): 
        p_dic.append([val,i])
    p_dic = sorted(p_dic,key=lambda x:(-x[0],x[1]))
    for i in g_dic:
        result = []
        c = 0
        for k in p_dic:
            if genres[k[1]] == i:
                c+=1
                if c>2:
                    break
                else:
                    result.append(k[1])
        answer += result
    return answer