n = int(input())
dp = [0] *(n+1)

def fib(n): 
  dp[1] =1
  dp[2] =1
  for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

fib(n)
print(dp[n], n-2)