import heapq
import sys
from collections import defaultdict

t = int(input())

for i in range(t):
    maxq = []
    minq = []
    maxlist = defaultdict(int)
    minlist = defaultdict(int)
    q = int(input())
    for j in range(q):
        li = sys.stdin.readline().rstrip().split()
        if li[0] == "I":
            heapq.heappush(maxq, -int(li[1]))
            heapq.heappush(minq, int(li[1]))
        else:
            if li[1] == "1":
                while maxq:
                    val = -heapq.heappop(maxq)
                    if minlist.get(val):
                        minlist[val] -= 1
                    else:
                        maxlist[val] += 1
                        break

            else:
                while minq:
                    val = heapq.heappop(minq)
                    if maxlist.get(val):
                        maxlist[val] -= 1
                    else:
                        minlist[val] += 1
                        break


    li = []
    while minq:
        val1 = heapq.heappop(minq)
        if maxlist.get(val1):
            maxlist[val1] -= 1
        else:
            li.append(val1)
    li.sort()
    if li :
        print(li[-1], li[0])
    else : print("EMPTY")

