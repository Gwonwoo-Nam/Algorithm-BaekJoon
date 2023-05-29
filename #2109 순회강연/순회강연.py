import sys
import heapq

n = int(input())

d = []

for i in range(n):
    val, date = map(int, sys.stdin.readline().rstrip().split())
    # 최대 힙
    heapq.heappush(d, (date, -val))

p = []
for i in range(1, n + 1):
    date, val = heapq.heappop(d)
    if len(p) < date :
        heapq.heappush(p, (-val, date))
    elif len(p) >= date:
        if -val > p[0][0] :
            heapq.heappop(p)
            heapq.heappush(p, (-val, date))
count = 0
for i in p :
    count += i[0]

print(count)