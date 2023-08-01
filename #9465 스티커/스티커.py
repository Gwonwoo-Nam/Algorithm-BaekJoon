t= int(input())

for i in range(t) :
  n = int(input())
  li = []
  li.append(list(map(int, input().split())))
  li.append(list(map(int, input().split())))

  dp = [[0 for i in range(n)] for j in range(2)]
  dp[0][0] = li[0][0]
  dp[1][0] = li[1][0]
  for i in range(1,n) :
    dp[0][i] = max(dp[0][i-1], dp[1][i-1] + li[0][i])
    dp[1][i] = max(dp[1][i-1], dp[0][i-1]+ li[1][i])
  print(max(dp[0][-1], dp[1][-1]))

    # dp 50 50  200 200 200
    # dp 30 100 120 160 260