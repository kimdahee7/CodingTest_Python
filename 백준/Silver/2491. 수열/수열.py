N = int(input())
l = list(map(int,input().split()))

dp1 = [1] * N
dp2 = [1] * N

# 증가하는 수열
for i in range(1,N):
    if l[i] >= l[i-1]:
            dp1[i] = max(dp1[i],dp1[i-1]+1)

# 감소하는 수열
for i in range(1,N):
    if l[i] <= l[i-1]:
            dp2[i] = max(dp2[i],dp2[i-1]+1)

max_data1 = max(dp1)
max_data2 = max(dp2)
print(max(max_data1,max_data2))