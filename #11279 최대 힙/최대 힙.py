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
            print(-heapq.heappop(q))
    else :
        heapq.heappush(q, -x)

