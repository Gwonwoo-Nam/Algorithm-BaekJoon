n = int(input())

arr = []
arr.append(0)
for i in range(n) :
    arr.append(int(input()))

dp = [0 for i in range(n+1)]
dp[0] = 0
dp[1] = arr[1]
if n==1 :
    print(arr[1])
else :
    dp[2] = arr[1] + arr[2]
    for i in range(3,n+1) :
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
    print(dp[n])

