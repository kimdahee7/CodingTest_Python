def main():  
  l = []
  T = int(input())
  for i in range(T):
    s = list(str(input()))
    sum = 0
    score = 0
    for j in s:
      if j == 'O':
        score +=1
        sum +=score
      else:
        score = 0
    l.append(sum)
  for i in l:
    print(i)

main()