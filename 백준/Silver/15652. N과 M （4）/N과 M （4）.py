N,M = map(int,input().split())
answer = []

def back(s):
  if len(answer) == M:
    print(" ".join(map(str,answer)))
    return 
  for i in range(s,N+1):
    answer.append(i)
    back(i)
    answer.pop()

back(1)