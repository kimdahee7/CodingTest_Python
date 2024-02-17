T = int(input())
for _ in range(T):
  N = int(input())
  l = list(map(int,input().split()))
  l = l[::-1]
  max = l[0]
  total = 0

  for i in range(1,N):
    if max < l[i]:
      max = l[i]
    total += max - l[i]
  print(total)