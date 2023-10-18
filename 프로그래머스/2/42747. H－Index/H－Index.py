def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations),-1,-1):
        count = 0
        for j in citations:
            if j >= i:
                count+=1
        if count >= i and len(citations)-count <=i:
            return i