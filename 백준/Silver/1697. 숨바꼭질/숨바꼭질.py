from collections import deque
N,K = map(int,input().split())
dist = [0] * 100001
q = deque()
q.append(N)

while q:
  x = q.popleft()
  if x == K:
    print(dist[x])
    break
  for i in (x-1,x+1,x*2):
    if 0<=i<100001 and dist[i] == 0:
      dist[i] = dist[x] + 1
      q.append(i)