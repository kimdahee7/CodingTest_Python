def solution(citations):
    answer = 0
    citations.sort()
    #[0,1,3,5,6]
    answer = len(citations)
    ind = 0
    while ind<len(citations):
        if citations[ind] >= answer:
            break
        else:
            ind +=1
            answer -=1
    return answer