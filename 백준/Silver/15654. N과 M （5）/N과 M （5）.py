N,M = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
answer = []
def back():
  if len(answer) == M:
    print(" ".join(map(str,answer)))
    return 
  for i in l:
    if i not in answer:
      answer.append(i)
      back()
      answer.pop()

back()