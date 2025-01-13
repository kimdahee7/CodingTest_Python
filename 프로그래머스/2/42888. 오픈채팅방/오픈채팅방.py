def solution(record):
    answer = []
    result = []
    dic = {}
    for r in record:
        if r[0] == "E":
            a,b,c = r.split()
            if b not in dic:
                dic[b] = c
                result.append([b,"님이 들어왔습니다."])
            else:
                dic[b] = c
                result.append([b,"님이 들어왔습니다."])
        elif r[0] == "L":
            a,b = r.split()
            result.append([b,"님이 나갔습니다."])
        else:
            a,b,c = r.split()
            dic[b] = c
    for i in result:
        answer.append(dic[i[0]] + i[1])
    return answer