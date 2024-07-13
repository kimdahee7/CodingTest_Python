import math
N = int(input())
M = int(input())
l = list(map(int,input().split()))

answer = 0

for i in range(len(l)):
    if len(l) == 1:
        answer =max(answer,l[i]-0, N-l[i])
    if i == 0:
        answer = max(answer,l[i] - 0)
    elif i == len(l) - 1:
        answer = max(answer,N - l[i])
    else:
        answer = max(answer,math.ceil((l[i+1]-l[i])/2))
print(answer)