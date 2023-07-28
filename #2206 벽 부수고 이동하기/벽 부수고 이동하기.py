import sys
from collections import deque
n,m = map(int, input().split())

board = []
for i in range(n) :
  board.append(list(map(int,sys.stdin.readline().rstrip())))

q = deque()
q.append((0,0,1,1))
move = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[[0,0] for j in range(m)] for i in range(n)]
visited[0][0] = [1,1]

ans = -1
while q :
  r,c,check,count = q.popleft()
  if r == n - 1 and c == m - 1 :
    ans = count
    break
  for dx, dy in move:

    if r+dx >= 0 and r+dx < n and c+dy >= 0 and c+dy < m :
      # 벽을 부순 상태에서 방문
      if check == 0 and visited[r+dx][c+dy][0] == 0 :
        if board[r+dx][c+dy] == 0 :
          q.append((r+dx,c+dy, 0, count+1))
          visited[r+dx][c+dy][0] = 1

      # 벽 안 부순 상태에서 방문
      elif check == 1 and (visited[r+dx][c+dy][0] == 0 or visited[r+dx][c+dy][1] == 0) :
        if board[r+dx][c+dy] == 0 :
          q.append((r+dx,c+dy, 1, count+1))
          visited[r+dx][c+dy][0] = 1
          visited[r+dx][c+dy][1] = 1

      # 벽인 경우 부수는 경우와 안 부수는 경우
      if (board[r+dx][c+dy] == 1 and check == 1) :
        q.append((r+dx,c+dy, 0, count+1))
        visited[r+dx][c+dy][0] = 1
      




print(ans)