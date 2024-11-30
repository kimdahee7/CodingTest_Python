import math
A,B = map(int,input().split())

MAX = 100000
prime = [True for i in range(MAX+1)]
prime[1] = False

for i in range(2,int(math.sqrt(MAX))+1):
    if prime[i]:
        j = 2
        while i*j <= MAX:
            prime[i*j] = False
            j += 1

answer = 0
for i in range(A,B+1):
    count = 0
    k = 2
    while k**2 <= i:
        if i % k == 0:
            count +=1
            i = i // k
        else:
            k +=1
    if i > 1:
        count+=1
    if prime[count]:
        answer +=1
print(answer)