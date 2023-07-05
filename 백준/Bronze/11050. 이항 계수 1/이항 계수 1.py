def main():
  N,K = map(int,input().split())
  g = N-K
  a=1
  b=1
  c=1
  for i in range(1,N+1):
    a = a*i
  for j in range(1,K+1):
    b = b*j
  for x in range(1, g+1):
    c = c*x
  print(a//(b*c))
main()