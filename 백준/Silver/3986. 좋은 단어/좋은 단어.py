import sys
input = sys.stdin.readline
def main():
  c = 0
  N = int(input())
  for _ in range(N):
    s = input().strip()
    f = ""
    l = []
    for i in s:
      if i == f and len(l) != 0:
        l.pop(len(l)-1)
        if len(l) != 0:
          f = l[len(l)-1]
      else:
        l.append(i)
        f = l[len(l)-1]
    if len(l) == 0:
      c +=1
  print(c)   
main()