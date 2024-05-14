import math
A,B = map(int,input().split())

n = int(math.sqrt(B))+1
l = [True for _ in range(n+1)]

#소수 판
for i in range(2, int(math.sqrt(n)) + 1):
    if l[i] == True:
        j = 2
        while i*j <= n:
            l[i*j] = False
            j +=1

answer = set()
for i in range(2,len(l)):
    if l[i] == True:
        k = 2
        while True:
            if B < i**k:
                break
            if A <= i**k and i**k <= B:
                answer.add(i**k)
                k +=1
            else:
                k +=1

print(len(answer))