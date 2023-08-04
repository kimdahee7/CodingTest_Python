def main():
  r = 0
  cor = ["c=","c-","dz=","d-","lj","nj","s=","z="]
  s = input()
  for i in cor:
    while True:
      if i in s:
        r +=1
        s = s.replace(i," ",1)
      if i not in s:
        break
  for j in s:
    if j != " ":
      r +=1
  print(r)
  
main()