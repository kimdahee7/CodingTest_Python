def main():
  wl = []
  list1 = []
  list2 = []
  R,C = map(int,input().split())
  for _ in range(R):
    s = input()
    list1.append(s)
  for i in range(C):
    word = ""
    for j in list1:
      word += j[i]
    list2.append(word)
  for z in list1:    
    if "#" in z:
      l = z.split("#")
      for j in l:
        if j != "#" and j != "":
          wl.append(j)
    else:
      wl.append(z)
  for z in list2:    
    if "#" in z:
      l = z.split("#")
      for j in l:
        if j != "#" and j != "":
          wl.append(j)
    else:
      wl.append(z)
  wl.sort()
  for i in wl:
    if len(i) !=1:
      print(i)
      break
main()