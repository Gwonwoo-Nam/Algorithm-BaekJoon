from collections import deque

n,m = map(int, input().split())

map = []
for i in range (n) :
    map.append(list(input()))

visited = [[0 for i in range(m)] for j in range(n)]
q = deque()
q.append((0,0,0))
move = [[1,0],[0,1],[-1,0],[0,-1]]
while len(q) > 0 :
    r, c, count = q.popleft()
    if r==n-1 and c == m-1 :
        print(count+1)
        break
    for dx,dy in move :
        if r+dx < n and r+dx >= 0 and c+dy < m and c+dy >= 0 :
            if map[r+dx][c+dy] == '1' and visited[r+dx][c+dy] == 0 :
                visited[r+dx][c+dy] = 1
                q.append((r+dx,c+dy,count+1))
