n = int(input())
l = [0]
for _ in range(n):
  l.append(int(input()))
dp = [0] * (n+1)

if n == 1:
  print(l[1])
  exit()
dp[0] = 0
dp[1] = l[1]
dp[2] = max(l[0]+l[2],l[1]+l[2])
for i in range(3,n+1):
  dp[i] = max(l[i]+dp[i-2],l[i]+l[i-1]+dp[i-3])
print(dp[n])