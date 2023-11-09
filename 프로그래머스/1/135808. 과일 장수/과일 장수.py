def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    n = m
    result = [score[i * n:(i + 1) * n] for i in range((len(score) + n - 1) // n )] 
    for i in result:
        if len(i) == m:
            answer += min(i) * m
    return answer