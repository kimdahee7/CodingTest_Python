def main():
  N = int(input())
  L = list(map(int, input().split()))
  y = 0
  m = 0
  for i in L:
    y += (i//30+1)*10
    m += (i//60+1)*15
  if(y>m):
    print("M", m)
  elif(m>y):
    print("Y", y)
  else:
    print("Y M", m)
 
main()