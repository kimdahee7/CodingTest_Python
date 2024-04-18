T = int(input())

def binary_search(l,i,start,end):
  index = -1
  while start <= end:
    mid = (start+end)//2
    if l[mid] < i:
      start = mid + 1
      index = mid
    elif l[mid] >= i:
      end = mid - 1
  if index == -1:
    return 0
  else:
    return index + 1
    
for _ in range(T):
  N,M = map(int,input().split())
  l_A = list(map(int,input().split()))
  l_B = list(map(int,input().split()))
  l_B.sort()
  answer = 0
  for i in l_A:
    start = 0
    end = len(l_B)-1
    answer += binary_search(l_B,i,start,end)
  print(answer)