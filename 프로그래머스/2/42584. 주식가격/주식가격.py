def solution(prices):
    answer = []
    for i in range(len(prices)):
        total = -1
        for j in range(i,len(prices)):
            if prices[i] <= prices[j]:
                total +=1
            else:
                total +=1
                break
        answer.append(total)
    return answer