N = int(input())
c = list(map(int,input().split()))
l = list(map(int,input().split()))        
total = c[0] * l[0]
stack = [l[0]]
for i in range(1,len(l)-1):
  if l[i] <= stack[-1]:
    total += (l[i] * c[i])
    stack.append(l[i])
  else:
    total += (stack[-1] * c[i])
print(total)