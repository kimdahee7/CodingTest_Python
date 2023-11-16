import math

def main(): 
  T = int(input())
  l = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
  for t in range(1,T+1):
    n,k = map(int,input().split())
    sl = {}
    for i in range(n):
      a,b,c = map(int,input().split())
      score = 0.35*a + 0.45*b + 0.2*c
      sl[i+1] = score
    sl = dict(sorted(sl.items(), key=lambda x:x[1], reverse=True))
    r = 1
    for i in sl:
      if i == k:
        break
      else:
        r+=1
    result = l[math.ceil(r/(n/10))-1]
    print("#"+str(t), result)
main()