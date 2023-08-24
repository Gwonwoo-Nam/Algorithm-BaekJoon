import math

n,m,l = map(int, input().split())
cur_stores = list(map(int, input().split()))

left = 0
right = 1001
q = []
cur_stores.sort()
cur_stores.insert(0, 0)
cur_stores.append(l)
for i in range(len(cur_stores) - 1):
    q.append(cur_stores[i + 1] - cur_stores[i])

def check(mid, m) :
    count = 0
    for e in q:
        count += (e-1) // mid
    return count > m


while left + 1 < right :
    mid = (left+right)//2


    if check(mid, m) :
        left = mid
    else :
        right = mid

print(right)