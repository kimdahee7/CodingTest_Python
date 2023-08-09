import sys
input = sys.stdin.readline
def main():
  l = set()
  s = input().strip()
  for i in range(0,len(s)):
    for j in range(0,len(s)+1):
      r = s[i:j]
      l.add(r)
  print(len(l)-1)
main()