from collections import deque

N,K = map(int,input().split())
INF = 1e9
time = [INF for _ in range(100010)]
answer = []

q = deque()
q.append(N)
time[N] = 0
if N == K:
  answer.append(time[N])
while q:
  x = q.popleft()
  for i in x+1,x-1,2*x:
    if i < 0 or i >= 100010:
      continue
      
    if time[i] >= time[x] +1:
      time[i] = time[x] +1
      q.append(i)
      if i == K:
        answer.append(time[i])
      
print(time[K])
total = 0
for i in answer:
  if i == time[K]:
    total +=1
print(total)