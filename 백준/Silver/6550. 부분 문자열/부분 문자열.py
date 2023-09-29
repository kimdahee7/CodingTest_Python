def main():  
  while True:
    try:
      s,t = map(str,input().split())
      f = 0
      r = 0
      for i in s:
        e = len(t)
        if i in t[f:e]:
          t = t[t.index(i) +1:e]
        else:
          r +=1
          print("No")
          break
      if r == 0:
        print("Yes")
    except:
      break
main()