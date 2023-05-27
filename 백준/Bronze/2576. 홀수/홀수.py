def main():
  x1,x2,x3,x4,x5,x6,x7 = int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
  list = [x1,x2,x3,x4,x5,x6,x7]
  sum = 0
  list2 = []
  for i in list:
    if i%2 != 0:
      list2.append(i)
      sum = sum + i
  if sum == 0:
    print('-1')
  else:
    print(sum)
    print(min(list2))
    
main()