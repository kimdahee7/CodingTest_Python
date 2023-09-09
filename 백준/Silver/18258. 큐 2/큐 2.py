import sys
input = sys.stdin.readline
from collections import deque
def main(): 
  queue = deque()
  N = int(input())
  for i in range(N):
    s = input().split()
    if s[0] == "push":
      queue.append(s[1])
    if s[0] == "pop":
      if len(queue) == 0:
        print(-1)
      else:
        print(queue.popleft())
    if s[0] == "size":
      print(len(queue))
    if s[0] == "empty":
      if len(queue) == 0:
        print(1)
      else:
        print(0)
    if s[0] == "front":
      if len(queue) == 0:
        print(-1)
      else:
        print(queue[0])
    if s[0] == "back":
      if len(queue) == 0:
        print(-1)
      else:
        print(queue[-1])
main()