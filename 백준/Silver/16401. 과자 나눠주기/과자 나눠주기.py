def binary_search(start,end,l,M):
  length = 0
  while start <= end:
    total = 0
    mid = (start+end)//2
    for i in l:
      total += i//mid
    if total >= M:
      start = mid + 1
      length = mid
    else:
      end = mid - 1
  return length

M,N = map(int,input().split())
l = list(map(int,input().split()))
start = 1
end = max(l)
answer = binary_search(start,end,l,M)
print(answer)