import sys

n, k = map(int,input().split())

li = []
for i in range(n) :
    li.append(int(sys.stdin.readline().rstrip()))

count = 0
for i in reversed(li) :
    if k == 0 :
        break
    if k >= i :
        count += int(k/i)
        k = k%i

print(count)
