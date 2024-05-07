from collections import deque
N = int(input())
rock = list(map(int,input().split()))
S = int(input())
visited = [0] * N

q = deque()
q.append(S)
visited[S-1] = 1
count = 1
while q:
    x = q.popleft()
    for i in (x+rock[x-1],x-rock[x-1]):
        if 1<=i<=N and visited[i-1] == 0:
            visited[i-1] = 1
            count +=1
            q.append(i)

print(count)