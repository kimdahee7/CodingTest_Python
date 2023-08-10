import sys
input = sys.stdin.readline
from queue import PriorityQueue
def main():
  l = PriorityQueue()
  N = int(input())
  for _ in range(N):
    x = int(input())
    if x != 0:
      l.put((-x,x))
    else:
      if l.empty():
        print(0)
      else:
        print(l.get()[1])
main()