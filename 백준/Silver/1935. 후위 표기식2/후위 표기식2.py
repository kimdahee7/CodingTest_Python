import sys
input = sys.stdin.readline
def main(): 
  dic = {}
  l = []
  r = []
  total = 0
  N = int(input())
  s = input()
  for _ in range(N):
    d = int(input())
    l.append(d)
  for i in range(N):
    dic[chr(i+65)] = l[i]
  for z in s:
    if 'A' <= z <= 'Z' :
      r.append(dic[z])
    else:
      if len(r) ==1:
        break
      x = r.pop()
      y = r.pop()
      if z == "*":
        total = x*y
        r.append(total)
      elif z == "+":
        total = x+y
        r.append(total)
      elif z == "/":
        total = y/x
        r.append(total)
      elif z == "-":
        total = y-x
        r.append(total)
  print('%.2f' %r[0])
main()