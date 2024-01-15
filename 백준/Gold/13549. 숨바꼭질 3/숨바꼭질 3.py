from collections import deque

N,K = map(int,input().split())
INF = 1e9
time = [INF for _ in range(100010)]
q = deque()
q.append(N)
time[N] = 0
while q:
  x = q.popleft()
  for i in x+1,x-1,2*x:
    if i < 0 or i >= 100010:
      continue
      
    if i == 2*x and time[i] > time[x]:
      time[i] = time[x]
      q.append(i)
    if time[i] > time[x] +1:
      time[i] = time[x] +1
      q.append(i)

print(time[K])