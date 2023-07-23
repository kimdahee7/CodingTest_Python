import sys
input = sys.stdin.readline
from collections import deque
def main():
  l = deque()
  r = []
  N,K = map(int,input().split())
  for i in range(1,N+1):
    l.append(i)
  i = 0
  while len(l) != 0 :
    if i != K-1:
      l.append(l[0])
      l.remove(l[0])
      i +=1
    if i == K-1:
      r.append(l[0])
      l.popleft()
      i = 0 
  print("<", end="")
  for j in r:
    if j != r[len(r)-1]:
      print(j, end=", ")
    else:
      print(j, end=">")
main()