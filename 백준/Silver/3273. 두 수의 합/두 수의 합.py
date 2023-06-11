def main():
  n = int(input())
  l = sorted(list(map(int,input().split())))
  x = int(input())
  answer = 0
  left, right = 0, n-1 # 왼쪽, 오른쪽
  while left < right:
     temp = l[left] + l[right]
     if temp == x:
         answer += 1
         left += 1
     elif temp < x:
         left += 1
     else:
         right -= 1
  print(answer)
main()