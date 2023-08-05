import sys
input = sys.stdin.readline
def main():  
  l = []
  r = ""
  N = str(input())
  for i in N:
    l.append(i)
  l.sort(reverse=True)
  for j in l:
    r+=j
  print(int(r))
main()