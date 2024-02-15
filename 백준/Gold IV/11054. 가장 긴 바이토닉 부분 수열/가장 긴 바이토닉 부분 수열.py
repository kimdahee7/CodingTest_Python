N = int(input())
l = list(map(int,input().split()))
answer = []
dp1 = [1] * len(l)
for i in range(1,len(l)):
  for j in range(i):
    if l[i] > l[j]:
      dp1[i] = max(dp1[i],dp1[j] + 1)
l = l[::-1]
dp2 = [1] * len(l)
for i in range(1,len(l)):
  for j in range(i):
    if l[i] > l[j]:
      dp2[i] = max(dp2[i],dp2[j] + 1)

dp2 = dp2[::-1]
for i in range(len(l)):
  answer.append(dp1[i] + dp2[i] -1)
print(max(answer))