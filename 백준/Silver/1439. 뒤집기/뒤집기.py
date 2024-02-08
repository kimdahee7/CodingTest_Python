S = input()
total = 0
stack = [S[0]]
if S[0] == "0":
  a = 1
  b = 0
else:
  b = 1
  a = 0
for i in range(1,len(S)):
  if S[i] != stack[-1]:
    if S[i] == "1":
      b +=1
    else:
      a +=1
  stack.append(S[i])
print(min(a,b))