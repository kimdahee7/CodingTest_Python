def solution(n):
    answer = ''
    dic = {1:1,2:2,0:4}
    k = -1
    while True:
        if k == 0:
            n -=1
        if n == 0:
            break
        k = n%3
        n = n//3
        answer += str(dic[k])
    return answer[::-1]
