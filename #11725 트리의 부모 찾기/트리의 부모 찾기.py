import sys
from collections import deque

n = int(input())

q = deque()
q.append(1)
m = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
parent = [0 for i in range(n+1)]

for i in range(n-1) :
  a,b = map(int, sys.stdin.readline().rstrip().split())
  m[a].append(b)
  m[b].append(a)

visited[1] = 1

while q :
  e = q.popleft()
  for a in m[e] :
    if visited[a] == 0 :
      q.append(a)
      visited[a] = 1
      parent[a] = e

for i in range(2,len(parent)) :
  print(parent[i])
