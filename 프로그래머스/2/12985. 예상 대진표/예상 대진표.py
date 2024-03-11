def solution(n,a,b):
    answer = 0
    while True:
        answer +=1
        if abs(a-b) == 1 and a//2 != b//2:
            break
        else:
            if a%2 !=0:
                a =a//2 +1
            else:
                a = a//2
            if b%2 != 0:
                b = b//2 +1
            else:
                b = b//2
    return answer
