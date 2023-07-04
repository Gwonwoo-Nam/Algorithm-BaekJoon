
li = list(input().split("-"))

flag = False
ans = 0
for i in li :
    sum = 0
    for j in i.split("+") :
        sum += int(j)
    if flag :
        sum = -sum
    flag = True
    ans += sum

print(ans)
