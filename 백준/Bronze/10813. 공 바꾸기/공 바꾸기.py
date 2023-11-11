import sys
input = sys.stdin.readline

def main(): 
  N,M = map(int,input().split())
  b = [i for i in range(1,N+1)]
  for i in range(M):
    temp = 0
    i,j = map(int,input().split())
    temp = b[i-1]
    b[i-1] = b[j-1]
    b[j-1] = temp
  for j in b:
    print(j, end= " ")
main()