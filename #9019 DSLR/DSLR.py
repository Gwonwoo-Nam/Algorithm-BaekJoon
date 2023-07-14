from collections import deque
t = int(input())



def d(a) :
  a *= 2
  if a > 9999 :
    return a % 10000
  return a

def s(a) :
  if a == 0 :
    return 9999
  return a-1

def l(a) :
  tmp = int(a / 1000)
  a -= 1000*(tmp)
  a *= 10
  a += tmp
  return a


def r(a) :
  tmp = a % 10
  a = int(a / 10)
  a += tmp*1000
  return a

def bfs(a,b) :
  q = deque()
  visited = [0 for i in range(10001)]

  q.append((a,''))

  while q :
    a,command = q.popleft()
    if a == b :
      return command
    if visited[d(a)] == 0 :
      q.append((d(a),command + 'D'))
      visited[d(a)] = 1
    if visited[s(a)] == 0 :
      q.append((s(a),command + 'S'))
      visited[s(a)] = 1
    if visited[l(a)] == 0 :
      q.append((l(a),command + 'L'))
      visited[l(a)] = 1
    if visited[r(a)] == 0 :
      q.append((r(a),command + 'R'))
      visited[r(a)] = 1

for i in range(t) :
  a, b = map(int, input().split())
  print(bfs(a,b))