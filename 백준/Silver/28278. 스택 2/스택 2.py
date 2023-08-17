import sys
input = sys.stdin.readline
def main():
  l = []
  N = int(input())
  for _ in range(N):
    s = input().split()
    if s[0] == "1":
      l.append(s[1])
    if s[0] == "2":
      if len(l) == 0:
        print(-1)
      else:
        print(l.pop())
    if s[0] == "3":
      print(len(l))
    if s[0] == "4":
      if len(l) == 0:
        print(1)
      else:
        print(0)
    if s[0] == "5":
      if len(l) == 0:
        print(-1)
      else:
        print(l[-1])
main()