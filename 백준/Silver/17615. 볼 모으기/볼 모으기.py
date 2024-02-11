N = int(input())
l = input()
answer = []
def countR(l):
  total = 0
  s = 0
  for i in range(len(l)):
    if l[i] == "B":
      s = i
      break
  for i in range(s,len(l)):
    if l[i] == "R":
      total+=1
  return total

def countB(l):
  total = 0
  s = 0
  for i in range(len(l)):
    if l[i] == "R":
      s = i
      break
  for i in range(s,len(l)):
    if l[i] == "B":
      total+=1
  return total

answer.append(countR(l))
answer.append(countB(l))
l = l[::-1]
answer.append(countR(l))
answer.append(countB(l))
print(min(answer))