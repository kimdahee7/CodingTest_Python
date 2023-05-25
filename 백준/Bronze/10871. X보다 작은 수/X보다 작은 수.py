def main():
  N, X = map(int,input().split())
  solution(N, X)

def solution(N, X):
  A = list(map(int,input().split()))
  for i in A:
    if(i<X):
      print(i, end=" ")
    
main()