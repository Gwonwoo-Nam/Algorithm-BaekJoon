import sys

n = int(input())
arr = [[0 for j in range (n+1)] for i in range (n+1)]
dp = [[[0 for k in range(3)] for j in range (n+1)] for i in range (n+1)]
for i in range (1,n+1) :
    k = 1
    for j in map(int, sys.stdin.readline().rstrip().split()) :
        arr[i][k] = j
        k += 1;


dp[1][1][0] = 0
dp[1][2][0] = 1

for i in range (1,n+1) :
    for j in range (1,n+1) :
        if (i == 1 and j <= 2) :
            continue;
        if arr[i][j] == 0 :
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            if (arr[i][j] == 0 and arr[i][j-1] == 0 and arr[i-1][j] == 0) :
                dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[n][n]))
