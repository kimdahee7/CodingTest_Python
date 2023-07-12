import sys
input = sys.stdin.readline
def main():
  stack = []
  N = int(input())
  for i in range(N):
    s = input().split()
    if s[0] == "push":
      stack.append(s[1])
    if s[0] == "pop":
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
    if s[0] == "top":
      if len(stack) == 0:
        print("-1")
      else:
        print(stack[-1])
main()