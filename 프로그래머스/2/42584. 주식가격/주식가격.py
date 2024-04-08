def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        count = -1
        for j in range(i,n):
            if prices[i] <= prices[j]:
                count +=1
            else:
                count +=1
                break
        answer.append(count)
    return answer

