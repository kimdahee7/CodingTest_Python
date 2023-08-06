import sys
input = sys.stdin.readline
def main():
  dic = {}
  N,M = map(int,input().split())
  for i in range(1,N+1):
    s = input().strip()
    dic[str(i)] = s
    dic[s] = str(i)
  for j in range(M):
    q = input().strip()
    print(dic[q])
      
main()