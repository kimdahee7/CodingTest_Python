from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
l = [0] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    l[b] +=1

q = deque()
for i in range(1,N+1):
    if l[i] == 0:
        q.append(i)

answer = []
while q:
    x = q.popleft()
    answer.append(x)
    for i in graph[x]:
        l[i] -=1
        if l[i] == 0:
            q.append(i)

for i in answer:
    print(i, end=" ")