N = int(input())
l = list(map(int,input().split()))
dp = [1] * N
for i in range(1,len(l)):
  for j in range(i):
    if l[i] < l[j]:
      dp[i] = max(dp[i],dp[j] +1)
print(len(dp)-max(dp))