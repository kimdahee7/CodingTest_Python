def main():
  result = []
  T = int(input())
  for i in range(T):
    sum =""
    R,S = map(str,input().split())
    R = int(R)
    for i in S:
      sum +=i*R
    result.append(sum)
  for i in result:
    print(i)
main()