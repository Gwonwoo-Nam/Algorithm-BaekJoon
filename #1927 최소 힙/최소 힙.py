import heapq
import sys
n = int(input())

q = []
for i in range(n) :
    a = int(sys.stdin.readline().rstrip())
    if a == 0 :
        if len(q) > 0 :
            print(heapq.heappop(q))
        else :
            print(0)
    else :
        heapq.heappush(q, a)
