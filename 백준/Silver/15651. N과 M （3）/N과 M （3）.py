N,M = map(int,input().split())
answer = []
def back():
  if len(answer) == M:
    print(" ".join(answer))
    return 
  for i in range(1,N+1):
    answer.append(str(i))
    back()
    answer.pop()
  
back()