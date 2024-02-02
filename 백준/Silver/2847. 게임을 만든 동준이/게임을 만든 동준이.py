N = int(input())
score = []
for i in range(N):
  s = int(input())
  score.append(s)
score = score[::-1]
c = score[0]
total = 0
for i in range(1,len(score)):
  if score[i] < c:
    c = score[i]
    continue
  elif score[i] == c:
    c = score[i]-1
    total +=1
  else:
    k = score[i] - c +1
    c = c-1
    total += k
print(total)