import heapq

n,k = map(int, input().split())

visited = [0 for i in range(200001)]

q = []
heapq.heappush(q, (0,n))
visited[n] = 1

while q :
  count, pos = heapq.heappop(q)
  visited[pos] = 1
  if pos == k :
    print(count)
    break
  if pos * 2 <= 100000 and visited[pos*2] == 0:
    heapq.heappush(q,(count, pos*2))
  if pos + 1 <= 100000 and visited[pos+1] == 0:
    heapq.heappush(q,(count+1,pos+1))
  if pos -1 >= 0 and visited[pos-1] == 0:
    heapq.heappush(q,(count+1,pos-1))



