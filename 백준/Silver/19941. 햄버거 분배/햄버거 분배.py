N,K = map(int,input().split())
l = list(input())
total = 0
for i in range(N):
  if l[i] == "P":
    c = 0
    if 0>i-K:
      for j in range(0,i):
        if l[j] == "H":
          total+=1
          c+=1
          l[j] = "X"
          break
    elif 0<=i-K:
      for j in range(i-K,i):
        if l[j] == "H":
          total+=1
          c+=1
          l[j] = "X"
          break
    if i+K<N and c == 0:
      for j in range(i+1,i+K+1):
        if l[j] == "H":
          total +=1
          l[j] = "X"
          break
    if i+K>=N and c == 0:
      for j in range(i+1,N):
        if l[j] == "H":
          total +=1
          l[j] = "X"
          break

print(total)