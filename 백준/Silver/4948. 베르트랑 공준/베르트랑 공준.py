import math

n = 250000
l = [True for _ in range(n+1)]

#에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
    if l[i] == True:
        j = 2
        while i*j <= n:
            l[i*j] = False
            j +=1

while True:
    n = int(input())
    if n == 0:
        exit()
    answer = 0
    for i in range(n+1,2*n+1):
        if l[i]:
            answer +=1
    print(answer)