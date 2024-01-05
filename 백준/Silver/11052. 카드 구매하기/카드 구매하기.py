N = int(input())
l = list(map(int,input().split()))
l.insert(0,0)
dp = [0] * (N+1)
if N == 1:
  print(l[1])
  exit()
dp[0] = 0
dp[1] = l[1]
for i in range(2,N+1):
  for j in range(i):
    dp[i] = max(dp[i],dp[j]+l[i-j])
print(dp[N])