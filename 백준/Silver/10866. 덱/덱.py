import sys
from collections import deque
input = sys.stdin.readline
def main():
  stack = deque()
  N = int(input())
  for i in range(N):
    s = input().split()
    if s[0] == "push_back":
      stack.append(s[1])
    if s[0] == "push_front":
      stack.appendleft(s[1])
    if s[0] == "pop_front":
      if len(stack) == 0:
        print("-1")
      else:
        print(stack.popleft())
    if s[0] == "pop_back":
      if len(stack) == 0:
        print("-1")
      else:
        print(stack.pop())
    if s[0] == "size":
      print(len(stack))
    if s[0] == "empty":
      if len(stack) == 0:
        print("1")
      else:
        print("0")
    if s[0] == "front":
      if len(stack) == 0:
        print("-1")
      else:
        print(stack[0])
    if s[0] == "back":
      if len(stack) == 0:
        print("-1")
      else:
        print(stack[len(stack)-1])
main()