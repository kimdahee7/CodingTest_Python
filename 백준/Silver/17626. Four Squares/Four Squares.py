from itertools import product
n = int(input())
total = 0
l = []
l2 = []
i = 1
while (i**2<=n):
  l.append(i**2)
  i +=1
data = list(product(l,repeat=2))
for k in data:
  l2.append(sum(k))
result = 0
if n in l:
  result = 1
elif n in l2:
  result = 2
else:
  for x in l:
    if n-x in l2:
      result = 3
      break
if result == 0:
  print(4)
else:
  print(result)