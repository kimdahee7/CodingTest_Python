def main():
  x1 = list(map(int, input().split()))
  x2 = list(map(int, input().split()))
  x3 = list(map(int, input().split()))
  count(x1)
  count(x2)
  count(x3)

def count(x):
  sum = 0
  for i in x:
    if i == 0:
      sum = sum+1
  if sum == 0:
    print('E')
  elif sum == 1:
    print('A')
  elif sum == 2:
    print('B')
  elif sum == 3:
    print('C')
  else:
    print('D')
        
main()