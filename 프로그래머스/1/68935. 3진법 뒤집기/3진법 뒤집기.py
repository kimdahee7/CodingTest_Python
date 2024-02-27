def solution(n):
    answer = ""
    while n > 0:
        answer += str(n%3)
        n = n//3
    answer[::-1]
    result = int(answer,3)
    return result