N = int(input())
dic = {}
for _ in range(N):
  n = int(input())
  if n in dic:
    dic[n] += 1
  else:
    dic[n] = 1
dic = dict(sorted(dic.items(), key=lambda x:(x[1],-x[0]), reverse=True))
print(list(dic.keys())[0])