import sys

n = int(input())

tri = [[] for i in range(n)]
for _ in range(n):
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    for e in li :
        tri[_].append(e)

dp = [[] for i in range(n)]

dp[0].append(tri[0][0])
for r in range(1, len(tri)):
    for c in range(len(tri[r])):
        if c == 0:
            tmp = dp[r - 1][c] + tri[r][c]
        elif c >= len(tri[r]) - 1:
            tmp = dp[r - 1][c - 1] + tri[r][c]
        else:
            tmp = max(dp[r - 1][c], dp[r - 1][c - 1]) + tri[r][c]

        dp[r].append(tmp)

print(max(dp[n - 1]))
