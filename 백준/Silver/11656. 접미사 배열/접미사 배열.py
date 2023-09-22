import sys
input = sys.stdin.readline
def main():
  l = []
  w = input().strip()
  l.append(w)
  for i in w:
    w = w.replace(i,"",1)
    if w =="":
      break
    else:
      l.append(w)
  l.sort()
  for j in l:
    print(j)
main()