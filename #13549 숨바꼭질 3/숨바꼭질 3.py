from collections import deque

n,k = map(int, input().split())

visited = [0 for i in range(200001)]

q = deque()
q.append((n,0))
visited[n] = 1

while q :
  pos, count = q.popleft()
  tmp = pos
  if pos == k :
    print(count)
    break
  if pos * 2 <= 100000 and visited[pos*2] == 0:
    visited[pos*2] = 1
    q.append((pos*2,count))


  if pos -1 >= 0 and visited[pos-1] == 0:
    visited[pos-1] = 1
    q.append((pos-1, count+1))
  if pos + 1 <= 100000 and visited[pos+1] == 0:
    visited[pos+1] = 1
    q.append((pos+1, count+1))


