import sys
input = sys.stdin.readline
def main(): 
  l = []
  total = 0
  r = input()
  r = r.replace("()",".")
  for i in r:
    if i == "(":
      l.append(i)
    if i == ")":
      l.pop()
      total += 1
    if i == ".":
      total += len(l)
  print(total)
main()