import sys
input = sys.stdin.readline
def main():
  l = [0]*10001
  N = int(input())
  for _ in range(N):
    data = int(input())
    l[data] +=1
  for i in range(10001):
    if l[i] !=0:
      for j in range(l[i]):
        print(i)
main()