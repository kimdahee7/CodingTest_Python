import sys
input = sys.stdin.readline
def main():
  s = set()
  M = int(input())
  for i in range(M):
    c = input().split()
    if c[0] == "add":
      s.add(c[1])
    if c[0] == "remove":
      if c[1] in s:
        s.remove(c[1])
    if c[0] == "check":
      if c[1] in s:
        print(1)
      else:
        print(0)
    if c[0] == "toggle":
      if c[1] in s:
        s.remove(c[1])
      else:
        s.add(c[1])
    if c[0] == "all":
      s = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    if c[0] == "empty":
      s.clear()
main()