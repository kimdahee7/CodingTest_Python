def solution(s):
    answer = []
    cnt = -1
    l = []
    tmp = []
    num = ""
    k = 0
    for i in s:
        if cnt == 1 and i != "," and i != "}":
            num += i
        if i == "," and num != "":
            tmp.append(int(num))
            num = ""
        if i == "{":
            cnt +=1
        if i == "}":
            if num != "":
                tmp.append(int(num))
            if len(tmp) != 0:
                l.append(tmp)
                tmp = []
                cnt -=1
                num = ""
    l.sort(key=len)
    for i in l:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer