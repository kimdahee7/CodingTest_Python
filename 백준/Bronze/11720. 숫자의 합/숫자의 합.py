import sys
def main():
  N = int(sys.stdin.readline())
  x = list(map(int,sys.stdin.readline().rstrip()))
  print(sum(x))
main()