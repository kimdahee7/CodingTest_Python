N = int(input())
A = list(map(int,input().split()))
dp = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j] + 1)

answer = []
max_data = max(dp)
print(max_data)
max_index = dp.index(max_data)

for i in range(max_index,-1,-1):
    if dp[i] == max_data:
        answer.append(A[i])
        max_data -=1

for i in answer[::-1]:
    print(i,end=" ")