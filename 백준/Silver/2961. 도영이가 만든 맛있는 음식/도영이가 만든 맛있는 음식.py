from itertools import combinations
N = int(input())
c = [i for i in range(N)]
l = []
answer = []
for _ in range(N):
    a,b = map(int,input().split())
    l.append([a,b])

for i in range(1,N+1):
    combi = combinations(c,i)
    for com in combi:
        s = 1
        b = 0
        for co in com:
            s *= l[co][0]
            b += l[co][1]
        answer.append(abs(s-b))
print(min(answer))