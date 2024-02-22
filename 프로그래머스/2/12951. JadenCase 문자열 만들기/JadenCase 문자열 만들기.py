def solution(s):
    answer = []
    l = []
    word = ""
    for i in s:
        if i != " ":
            word += i
        else:
            if len(word) == 0:
                l.append(" ")
            else:
                l.append(word)
                word = ""
                l.append(" ")
    if len(word) != 0:
        l.append(word)
    for i in l:
        answer.append(i[0].upper() + i[1:len(i)].lower())
    return "".join(answer)