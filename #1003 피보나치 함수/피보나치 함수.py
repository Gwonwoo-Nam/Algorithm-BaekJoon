
dp1 = [0 for i in range (41)]
dp2 = [0 for i in range (41)]

dp1[0] = 1
dp1[1] = 0
dp2[0] = 0
dp2[1] = 1
for n in range(2,41) :
    dp1[n] = dp1[n-1] + dp1[n-2]
    dp2[n] = dp2[n-1] + dp2[n-2]

t = int(input())

for i in range (t) :
    n = int(input())

    print(str(dp1[n]) +" " +str(dp2[n]))
