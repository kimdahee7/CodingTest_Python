A = int(input())
l = list(map(int,input().split()))
dp = [0] * A
for i in range(A):
    dp[i] = l[i]
for i in range(1,A):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i],dp[j]+l[i])
print(max(dp))