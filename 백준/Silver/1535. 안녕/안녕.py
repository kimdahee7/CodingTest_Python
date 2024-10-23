from itertools import combinations

N = int(input())
power = list(map(int,input().split()))
happy = list(map(int,input().split()))
l = [i for i in range(N)]
answer = []

for i in range(1,N+1):
    combi = combinations(l,i)
    for c in combi:
        total_power = 0
        total_happy = 0
        for j in c:
            total_power+=power[j]
            total_happy+=happy[j]
        if total_power < 100:
            answer.append(total_happy)
answer.sort()
if len(answer) == 0:
    print(0)
else:
    print(answer[-1])