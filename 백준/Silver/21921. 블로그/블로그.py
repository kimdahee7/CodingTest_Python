import sys
input = sys.stdin.readline
def main(): 
  r = []
  N,X = map(int,input().split())
  l = list(map(int,input().split()))
  n = len(l)
  window = sum(l[:X])
  r.append(window)
  result = window
  for i in range(X,n):
    window +=l[i] - l[i-X]
    r.append(window)
    result = max(result,window)
  if result == 0:
    print("SAD")
  else:
    print(result)
    print(r.count(result))
main()