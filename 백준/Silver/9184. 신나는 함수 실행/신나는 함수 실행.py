dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for i in range(0,21):
  for j in range(0,21):
    for z in range(0,21):
      if i<=0 or j<=0 or z<=0:
        dp[i][j][z] = 1
      elif i<j and j<z:
        dp[i][j][z] = dp[i][j][z-1]+dp[i][j-1][z-1]-dp[i][j-1][z]
      else:
        dp[i][j][z] = dp[i-1][j][z] + dp[i-1][j-1][z] + dp[i-1][j][z-1] - dp[i-1][j-1][z-1]
while True:
  a,b,c = map(int,input().split())
  if a == -1 and b == -1 and c == -1:
    break
  if a<=0 or b<=0 or c<=0:
    dp[a][b][c] = 1
  elif a>20 or b>20 or c>20 and dp[a][b][c] == 0:
    dp[a][b][c] = dp[20][20][20]
  print("w("+str(a)+", "+str(b)+", "+str(c)+") = "+str(dp[a][b][c]))