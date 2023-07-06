import heapq
import sys

n = int(input())

q = []
for i in range(n) :
    x = int(sys.stdin.readline().rstrip())
    if x == 0 :
        if not q :
            print(0)
        else :
            val, pos = heapq.heappop(q)
            print(val*pos)
    else :
        if x > 0 :
            heapq.heappush(q, (x, 1))
        else :
            heapq.heappush(q, (-x, -1))

