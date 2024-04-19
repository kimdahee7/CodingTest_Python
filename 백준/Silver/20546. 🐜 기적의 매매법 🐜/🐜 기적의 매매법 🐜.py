def Jun(M,l):
  count = 0
  for i in range(len(l)):
    count += M//l[i]
    M -= (l[i]*(M//l[i]))
  return count*l[len(l)-1] + M

def Sung(M,l):
  count = 0
  a = 0
  d = 0
  for i in range(1,len(l)):
    if l[i-1] > l[i]:
      d +=1
      a = 0
    elif l[i-1] < l[i]:
      d = 0
      a +=1
    else:
      a = 0
      d = 0
    if d >= 3:
      count += M//l[i]
      M -= l[i]*(M//l[i])
    if a >= 3:
      M += count*l[i]
      count = 0
  return count * l[len(l)-1] + M

M = int(input())
l = list(map(int,input().split()))
a = Jun(M,l)
b = Sung(M,l)

if a>b:
  print("BNP")
elif b>a:
  print("TIMING")
else:
  print("SAMESAME")