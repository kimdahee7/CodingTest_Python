import sys
input = sys.stdin.readline
def main():  
  total = 0
  dic = {}
  while True:
    n = input().strip()
    if not n: 
      break
    total += 1
    if n in dic:
      dic[n] += 1
    else:
      dic[n] = 1
  dic = dict(sorted(dic.items()))
  for key, value in dic.items():
    print('%s %.4f'%(key,value/total*100))

main()