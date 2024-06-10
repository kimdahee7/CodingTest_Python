X,Y = map(int,input().split())
def binary(X,Y):
  start = 0
  end = 1000000000
  Z = Y* 100//X
  if Z >= 99:
    print(-1)
    exit()
  while start <= end:
    mid = (start + end)//2
    k = (Y+mid)* 100 // (X+mid)
    if k > Z:
      end = mid - 1
    else:
      start = mid + 1
  print(start)

binary(X,Y)