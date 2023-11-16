from collections import Counter

def main(): 
  T = int(input())
  for _ in range(1,T+1):
    t = int(input())
    score = list(map(int,input().split()))
    c = dict(Counter(score))
    v = list(c.values())
    max_data = max(v)
    result = []
    for k,v in c.items():
      if v == max_data:
        result.append(k)
    print("#"+str(t),max(result))
main()
