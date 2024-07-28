import math
G = int(input())
list = [i**2 for i in range(1,100001)]

start = 0
end = 1
N = len(list)
answer = []
while start <= end and start < N and end < N:
    k = list[end] - list[start]
    if k == G:
        answer.append(int(math.sqrt(list[end])))
        start +=1
        end +=1
    elif k < G:
        end +=1
    else:
        start +=1

if not answer:
    print(-1)
else:
    for i in answer:
        print(i)