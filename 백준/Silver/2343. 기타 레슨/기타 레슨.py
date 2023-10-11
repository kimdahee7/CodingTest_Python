def main():
  N,M = map(int,input().split())
  l = list(map(int,input().split()))
  binary(l,M)

def binary(l,M):
  start = max(l)
  end = sum(l)
  while start <= end:
    count = 1
    total = 0
    mid = (start+end)//2
    for i in l:
      if total + i > mid:
        count +=1
        total = 0
      total += i
    if count <= M:
      answer = mid
      end = mid - 1
    else:
      start = mid + 1
  print(answer)
main()