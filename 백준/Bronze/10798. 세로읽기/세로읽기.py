def main():  
  l = []
  result = ""
  for _ in range(5):
    s = input()
    l.append(s)
  for i in range(15):
    for j in l:
      if len(j) > i:
        result += j[i]
  print(result)
main()