import sys
input = sys.stdin.readline
def main(): 
  l = []
  dic = {}
  N, M = map(int,input().split())
  for _ in range(N):
    word = input().strip()
    if len(word) >= M:
      l.append(word)
  l.sort()
  l.sort(key=len,reverse=True)
  for i in l:
    if i in dic:
      dic[i] +=1
    else:
      dic[i] = 1
  dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
  for y in dic.keys():
    print(y)
main()