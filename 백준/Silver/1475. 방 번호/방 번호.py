def main():
  countL = []
  x = input()
  n1 = x.count(str("9"))
  n2 = x.count(str("6"))
  sum = n1 + n2
  if sum%2 == 0:
    sum = sum//2
  else:
    sum = sum//2 +1
  for i in range(10):
    if i != 9 and i !=6:
      n3 = x.count(str(i))
      countL.append(n3)
  countL.append(sum)
  print(max(countL))
       
main()