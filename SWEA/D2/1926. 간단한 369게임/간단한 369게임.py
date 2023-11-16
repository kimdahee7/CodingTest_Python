def main(): 
  N = int(input())
  result = []
  l = {"3", "6", "9"}
  for i in range(1,N+1):
    count = 0
    for j in l:
      count += str(i).count(j)
    if count > 0:
      result.append("-"*count)
    else:
      result.append(i)
  for k in result:
    print(k,end=" ")
main()