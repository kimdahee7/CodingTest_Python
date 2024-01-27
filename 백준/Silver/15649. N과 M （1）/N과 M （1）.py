N,M = map(int,input().split())
answer = []
def back():
  if len(answer) == M:
    print(" ".join(answer))
  for i in range(1,N+1):
    if str(i) not in answer:
      answer.append(str(i))
      back()
      answer.pop()
  
back()