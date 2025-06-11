def factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

T = int(input())
answer = 0
for _ in range(T):
    n,m = map(int,input().split())
    answer = factorial(m)//(factorial(m-n)*factorial(n))
    print(answer)