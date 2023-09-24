import sys
input = sys.stdin.readline
def main():
  while True:
    s = input().strip()
    if s == "*":
      break
    total = 0
    for i in range(len(s)-1):
      check = set()
      for j in range(len(s)-(i+1)):
        d = s[j] + s[j+(i+1)]
        if d in check:
          print(s + " is NOT surprising.")
          total +=1
          break
        else:
          check.add(d)
      if total != 0:
        break
    if total == 0:
      print(s + " is surprising.")
            
main()