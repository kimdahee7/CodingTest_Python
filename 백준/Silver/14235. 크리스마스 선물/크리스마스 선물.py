from queue import PriorityQueue
def main():
  n = int(input())
  p = []
  v = PriorityQueue()
  for i in range(n):
    l = list(map(int,input().split()))
    p.append(l)
  for i in p:
    if i[0] == 0:
      if v.empty():
        print(-1)
      else:
        print(v.get()[1])
    else:
      for j in range(1,len(i)):
        v.put((-i[j],i[j]))
main()