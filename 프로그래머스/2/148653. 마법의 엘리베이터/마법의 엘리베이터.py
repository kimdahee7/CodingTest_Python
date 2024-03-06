def solution(storey):
    answer = 0
    while storey != 0:
        k = storey%10
        if k == 5:
            answer += 5
            storey = storey//10
            if storey%10 >=5:
                storey += 1
        elif k >5:
            answer += (10-k)
            storey = storey//10 +1
        else:
            answer += k
            storey = storey//10
    return answer