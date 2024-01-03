n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))
dp = [0] * n
if n == 1:
  print(l[0])
  exit()
if n == 2:
  print(l[0]+l[1])
  exit()
dp[0] = l[0]
dp[1] = l[0] + l[1]
dp[2] = max(l[0]+l[2],l[1]+l[2],dp[1])
for i in range(3,n):
  dp[i] = max(l[i]+dp[i-2],dp[i-1],l[i]+l[i-1]+dp[i-3])
print(max(dp))