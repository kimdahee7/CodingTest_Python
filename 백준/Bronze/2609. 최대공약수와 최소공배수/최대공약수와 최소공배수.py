def main():
  al = []
  bl = []
  r= []
  a,b = map(int,input().split())
  for i in range(1,a+1):
    if a%i == 0:
      al.append(i)
  for j in range(1,b+1):
    if b%j == 0:
      bl.append(j)
  for x in al:
    if x in bl:
      r.append(x)
  print(max(r))
  print(a//max(r)*b//max(r)*max(r))
main()