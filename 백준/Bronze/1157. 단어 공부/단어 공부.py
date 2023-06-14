def main():
  sum = 0
  listA = []
  list = []
  x = str(input()).upper()
  for i in range(ord('A'), ord('Z')+1):
    listA.append(chr(i))
    list.append(x.count(chr(i)))
  for i in list:
    if i == max(list):
      sum +=1
  if sum == 1:
    result = list.index(max(list))
    print(listA[result])
  else:
    print("?")
  
main()