import sys
input = sys.stdin.readline
def main():
  l = []
  r = ""
  s = input().strip()
  for i in s:
    if i == ">":
      r +=i
      l.append(r)
      r = ""
    elif i == " ":
      if "<" not in r:
        l.append(r[::-1])
        l.append(i)
        r = ""
      else:
        r +=i
    elif i == "<":
      if len(r) != 0:
        l.append(r[::-1])
        r = ""
        r += i
      else:
        r += i
    else:
      r +=i
  if len(r) != 0:
    l.append(r[::-1])
  for j in l:
    print(j,end="")
        
main()