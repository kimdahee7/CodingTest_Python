import sys
input = sys.stdin.readline

def fib(n):
  if n >= len(z):
    for i in range(len(z),n+1):
      z.append(z[i-1]+z[i-2])
      f.append(f[i-1]+f[i-2])
    
T = int(input())
for _ in range(T):
  z = [1,0,1]
  f = [0,1,1]
  n = int(input())
  fib(n)
  print(z[n],f[n])