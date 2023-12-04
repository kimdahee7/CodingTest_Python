A,B = map(int,input().split())
l = [B]
total = 0
while True:
  tmp = []
  total += 1
  for i in l:
    if i %10 == 1:
      tmp.append(i//10)
    else:
      if i%2 == 0:
        tmp.append(i//2)
      else:
        tmp = [0]
  l = tmp
  if A in l:
    print(total+1)
    break
  if max(l) <= A:
    print(-1)
    break