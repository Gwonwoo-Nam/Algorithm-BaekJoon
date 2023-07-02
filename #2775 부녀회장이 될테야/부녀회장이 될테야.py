def people(k, n) :
  dp = [[0 for i in range(15)] for j in range(15)]
  for i in range(1,n+1) :
    dp[0][i] = i
  for i in range(1, k+1) :
    for j in range(1, n+1) :
      for t in range(1, j+1) :
        dp[i][j] += dp[i-1][t]
  return dp[k][n]

t = int(input())
for i in range(t) :
  k = int(input())
  n = int(input())
  print(people(k, n))