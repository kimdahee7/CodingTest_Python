def main():
  resultL = []
  N = int(input())
  for i in range(N):
    x,y = map(str, input().split())
    listx = sorted(list(x))
    listy = sorted(list(y))
    if listx == listy:
      resultL.append("Possible")
    else: 
      resultL.append("Impossible")
  for i in range(N):
    print(resultL[i])
  
main()