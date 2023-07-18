import sys
input = sys.stdin.readline
def main():
  l = []
  N = int(input())
  for i in range(5000000):
    if '666' in str(i):
      l.append(int(i))
  print(l[N-1])
  
main()