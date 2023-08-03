def main():
  r = 0
  N = int(input())
  for _ in range(N):
    s = input()
    l = []
    for i in s:
      if i not in l:
        l.append(i)
      else:
        if l[len(l)-1] == i:
          l.append(i)
        else:
          r +=1
          break
  print(N-r) 
main()