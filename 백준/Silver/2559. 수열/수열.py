N,K = map(int,input().split())
l = list(map(int,input().split()))
window = sum(l[0:K])
answer = window
for i in range(K,len(l)):
  window -= l[i-K]
  window += l[i]
  answer = max(answer,window)
print(answer)