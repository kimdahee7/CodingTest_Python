import heapq
def main():
  heap = []
  n = int(input())
  for i in range(n):
    l = list(map(int,input().split()))
    for j in l:
      if n > len(heap):
        heapq.heappush(heap,j)
      else:
        if j > heap[0]:
          heapq.heappop(heap)
          heapq.heappush(heap,j)
  print(heap[0])
main()