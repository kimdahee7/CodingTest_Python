def main(): 
  T = int(input())
  for t in range(1,T+1):
    s = list(input())
    d = ["0" for i in range(len(s))]
    c = 0
    for i in range(len(s)):
      if d[i] != s[i]:
        c+=1
        for j in range(i,len(s)):
          d[j] = s[i]
        if d == s:
          break 
    print("#"+str(t), c)
main()
