def solution(n):
    answer = 0
    n_c = f(n)
    n = n +1
    while True:
        if n_c == f(n):
            answer = n
            break
        else:
            n = n + 1
    return answer

def f(n):
    total = 1
    while n != 1:
        if n % 2 == 1:
            total+=1
        n = n//2
    return total