from itertools import combinations
N,S = map(int,input().split())
l = list(map(int,input().split()))
c = []
for i in range(1,N+1):
    c.append(list(combinations(l,i)))
answer= 0
for i in c:
    for j in range(len(i)):
        if sum(list(i[j])) == S:
            answer +=1
print(answer)