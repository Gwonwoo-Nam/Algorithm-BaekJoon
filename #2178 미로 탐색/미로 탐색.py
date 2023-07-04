from collections import deque

n,m = map(int, input().split())

map = []
for i in range (n) :
    map.append(list(input()))

visited = [[0 for i in range(m)] for j in range(n)]
q = deque()
q.append((0,0,0))
while len(q) > 0 :
    r, c, count = q.popleft()
    if r==n-1 and c == m-1 :
        print(count+1)
        break
    if r+1 < n and map[r+1][c] == '1' and visited[r+1][c] == 0 :
        visited[r+1][c] = 1
        q.append((r+1,c,count+1))
    if c+1 < m and map[r][c+1] == '1' and visited[r][c+1] == 0:
        visited[r][c+1] = 1
        q.append((r,c+1,count+1))
    if r-1 >= 0 and map[r-1][c] == '1' and visited[r-1][c] == 0:
        visited[r-1][c] = 1
        q.append((r-1,c,count+1))
    if c-1 >= 0 and map[r][c-1] == '1' and visited[r][c-1] == 0:
        visited[r][c-1] = 1
        q.append((r,c-1,count+1))
