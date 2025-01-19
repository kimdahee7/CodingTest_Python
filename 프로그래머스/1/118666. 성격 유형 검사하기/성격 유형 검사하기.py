dic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
def solution(survey, choices):
    answer = ''
    #선택지 별 점수 
    score = [3,2,1,0,1,2,3]
    for i in range(len(survey)):
        first = survey[i][0]
        second = survey[i][1]
        ind = choices[i] -1
        if 0<= ind <3:
            dic[first] += score[ind]
        else:
            dic[second] += score[ind]
    answer += type("R","T")
    answer += type("C","F")
    answer += type("J","M")
    answer += type("A","N")
    return answer

def type(a,b):
    if dic[a] >= dic[b]:
        return a
    else:
        return b
        