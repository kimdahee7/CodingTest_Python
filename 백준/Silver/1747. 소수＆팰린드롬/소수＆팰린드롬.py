import math
N = int(input())

prime = [0] * 1003002
prime[1] = 1
for i in range(2,int(math.sqrt(1003002))+1):
    if prime[i] == 0:
        k = 2
        while i*k < 1003002:
            prime[i*k] = 1
            k +=1

for i in range(N,1003002):
    i = str(i)
    if i == i[::-1] and prime[int(i)] == 0:
        print(i)
        exit()