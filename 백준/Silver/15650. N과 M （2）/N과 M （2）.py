from itertools import combinations
N,M = map(int,input().split())
l = []
for i in range(1,N+1):
  l.append(i)
answer = list(combinations(l,M))
for a in answer:
  for b in a:
    print(b,end=" ")
  print()