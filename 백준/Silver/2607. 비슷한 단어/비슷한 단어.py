N = int(input())
word_list = [input() for _ in range(N)]
word = list(word_list[0])
answer = 0
for i in range(1,N):
  if abs(len(word_list[i])-len(word)) > 1:
    continue
  l = list(word_list[i])
  count = 0
  for j in word:
    if j in l:
      l.remove(j)
    else:
      count +=1
  if count > 1:
    continue
  elif len(l) == 0 or len(l) == 1:
    answer +=1
print(answer)