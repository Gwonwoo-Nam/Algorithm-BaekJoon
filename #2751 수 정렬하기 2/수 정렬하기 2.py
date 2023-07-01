import sys
import heapq

n = int(input())
heap = []

for i in range (n) :
  heapq.heappush(heap, int(sys.stdin.readline().rstrip()))

for i in range (n) :
  print(heapq.heappop(heap))