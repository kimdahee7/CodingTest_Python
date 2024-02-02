n,m = map(int,input().split())
l = list(map(int,input().split()))
c = 0
while c < m:
  l.sort()
  a = l[0] + l[1]
  l.pop(0)
  l.pop(0)
  l.append(a)
  l.append(a)
  c+=1
print(sum(l))