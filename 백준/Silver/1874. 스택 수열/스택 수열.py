import sys
input = sys.stdin.readline
def main():
  l = []
  r = []
  p = []
  start = 1
  n = int(input())
  for _ in range(n):
    data = int(input())
    l.append(data)
  for i in l:
    while True :
      if len(r) == 0:
        r.append(start)
        p.append("+")
        start +=1
      else:
        if i == r[len(r)-1]:
          r.pop()
          p.append("-")
          break
        else:
          if start > n :
            p.append("NO")
            break
          else:
            r.append(start)
            p.append("+")
            start +=1
  if "NO" in p:
    print("NO")
  else:
    for t in p:
      print(t)
    
main()