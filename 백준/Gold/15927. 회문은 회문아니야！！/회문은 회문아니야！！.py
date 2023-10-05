import sys
input = sys.stdin.readline
def main():  
  s = input().strip()
  if s == s[::-1]:
    n = s.replace(s[0],"")
    if n == "":
      print(-1)
    elif len(s) == 1:
      print(-1)
    else:
      print(len(s)-1)
  else:
    print(len(s))
main()