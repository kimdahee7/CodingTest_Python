def solution(str1, str2):
    w = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    answer = 0
    union = 0 #합집합 
    intersect = 0 #교집합
    w1 = {}
    w2 = {}
    for s in range(len(str1)-1):
        tmp = ""
        if str1[s].upper() in w and str1[s+1].upper() in w:
            tmp += str1[s].upper()
            tmp += str1[s+1].upper()
            if tmp in w1:
                w1[tmp] +=1
            else:
                w1[tmp] = 1
    for s in range(len(str2)-1):
        tmp = ""
        if str2[s].upper() in w and str2[s+1].upper() in w:
            tmp += str2[s].upper()
            tmp += str2[s+1].upper()
            if tmp in w2:
                w2[tmp] +=1
            else:
                w2[tmp] = 1
    #교집합 구하기 
    for i in w1:
        if i in w2:
            intersect += min(w1[i],w2[i])
    #합집합 구하기 
    for i in w1:
        if i in w2:
            union += max(w1[i],w2[i])
        else:
            union += w1[i]
    for i in w2:
        if i not in w1:
            union += w2[i]
    if union == 0 and intersect == 0:
        answer = 65536
        return answer 
    else:
        answer = (intersect/union * 65536)//1
        return answer