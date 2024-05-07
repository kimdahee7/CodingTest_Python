N,K = map(int,input().split())
backpack = []
value = []
dp = [0 for _ in range(K+1)]
for _ in range(N):
    W,V = map(int,input().split())
    backpack.append(W)
    value.append(V)
for i in range(N):
    for j in range(K,0,-1):
        if backpack[i] <=j:
            dp[j] = max(dp[j],dp[j-backpack[i]] + value[i])

print(dp[K])