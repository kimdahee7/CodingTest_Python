n = int(input())
answer = 0
while True:
    if n%5 == 0:
        answer += n//5
        break
    if n == 0:
        break
    if n <0:
        answer = -1
        break
    n -= 2
    answer +=1
print(answer)