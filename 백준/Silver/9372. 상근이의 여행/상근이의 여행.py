from collections import deque

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    route = [[] for _ in range(N+1)]
    airplane = 1
    for _ in range(M):
        a,b = map(int,input().split())
        route[a].append((b,airplane))
        route[b].append((a,airplane))
        airplane +=1
    answer = 1e9
    l = set()
    for start in range(1,N+1):
        visited = [0 for _ in range(N + 1)]
        q = deque()
        q.append(start)
        visited[start] = 1
        while q:
            x = q.popleft()
            for depart,num in route[x]:
                if not visited[depart]:
                    visited[depart] = 1
                    l.add(num)
                    q.append(depart)
        answer = min(answer,len(l))
    print(answer)