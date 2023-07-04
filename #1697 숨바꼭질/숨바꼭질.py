from collections import deque
n, k = map(int, input().split())

q = deque()
dp = [0 for i in range(100001)]
q.append(n)
while dp[k] == 0 and len(q) > 0:
    i = q.popleft()
    if i+1 <= 100000 and dp[i+1] == 0 :
        dp[i+1] = dp[i] + 1
        q.append(i+1)
    if i-1 >= 0 and dp[i-1] == 0:
        dp[i-1] = dp[i] + 1
        q.append(i-1)
    if 2*i <= 100000 and dp[2*i] == 0:
        dp[2*i] = dp[i] + 1
        q.append(2*i)
if n == k :
    print(0)
else :
    print(dp[k])
