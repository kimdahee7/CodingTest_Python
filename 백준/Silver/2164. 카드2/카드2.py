import sys
from collections import deque
def main():
  input = sys.stdin.readline
  stack = deque()
  N = int(input())
  for i in range(1,N+1):
    stack.append(i)
  while len(stack) != 1:
    stack.append(stack[1])
    stack.popleft()
    stack.popleft()
    if len(stack) == 2:
      stack.popleft()
      break
  print(stack[0])
main()