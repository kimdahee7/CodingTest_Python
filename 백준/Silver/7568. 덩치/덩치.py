def main():  
  l = []
  N = int(input())
  for i in range(N):
    X =list(map(int,input().split()))
    l.append(X)
  for j in range(N):
    sum = 0
    for r in range(N):
      if l[j][0] < l[r][0] and l[j][1] < l[r][1]:
        sum +=1
    print(sum+1, end=" ")
    
main()