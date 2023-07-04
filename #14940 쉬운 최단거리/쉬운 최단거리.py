from collections import deque
import sys
n,m = map(int, input().split())

board = []
for i in range(n) :
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

q = deque()
move = [[1,0], [0,1], [-1,0], [0,-1]]
visited = [[0 for i in range(m)] for j in range(n)]
ans = [[0 for i in range(m)] for j in range(n)]

for row in range (n) :
    for col in range(m) :
        if board[row][col] == 2 :
            q.append((row,col,0))
            visited[row][col] = 1

while q :
    row, col, count = q.popleft()
    ans[row][col] = count


    for dx, dy in move :
        if row+dx < n and row+dx >= 0 and col+dy < m and col+dy >= 0 :
            if visited[row+dx][col+dy] == 0 and board[row+dx][col+dy] != 0 :
                visited[row+dx][col+dy] = 1
                q.append((row+dx, col+dy, count+1))


for row in range (n) :
    for col in range(m) :
        if board[row][col] == 1 and visited[row][col] == 0:
            ans[row][col] = -1

for i in ans :
    print(" ".join(map(str, i)))
