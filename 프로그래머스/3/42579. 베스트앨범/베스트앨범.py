def solution(genres, plays):
    answer = []
    n = len(genres)
    l = {}
    g = {}
    for i in range(n):
        if genres[i] not in g:
            g[genres[i]] = plays[i]
        else:
            g[genres[i]] += plays[i]
    g = sorted(g,key=lambda x:g[x], reverse=True)
    for i in range(n):
        l[i] = plays[i]
    l = dict(sorted(l.items(),key=lambda x:x[1], reverse=True))
    for i in g:
        c = 0
        for j in l:
            if c == 2:
                break
            elif i == genres[j]:
                c +=1
                answer.append(j)    
    return answer