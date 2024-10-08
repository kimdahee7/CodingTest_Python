from collections import deque

N = int(input())
answer = []
relation = [[] for _ in range(N+1)]

while True:
    a,b = map(int,input().split())
    if a == -1 and b ==-1:
        break
    else:
        relation[a].append(b)
        relation[b].append(a)

for i in range(1,N+1):
    visited = [0 for _ in range(N+1)]
    q = deque()
    for j in relation[i]:
        q.append((j,1))
        visited[j] = 1
    while q:
        x,cnt = q.popleft()
        for k in relation[x]:
            if visited[k] == 0:
                q.append((k,cnt+1))
                visited[k] = cnt+1
    visited[i] = 0
    answer.append(max(visited))

min_data = min(answer)
print(min_data,answer.count(min_data))
for i in range(N):
    if answer[i] == min_data:
        print(i+1,end=" ")