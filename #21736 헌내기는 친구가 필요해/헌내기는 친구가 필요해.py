from collections import deque
n,m = map(int, input().split())

li = []
for i in range (n) :
    li.append(list(input()))
visited = [[0 for i in range(m)] for j in range(n)]

q = deque()

for i in range(len(li)) :
    for j in range(len(li[0])) :
        if li[i][j] == "I" :
            q.append((i,j))
            visited[i][j] = 1
        elif li[i][j] == "X" :
            visited[i][j] = 1

move = [[1,0],[0,1],[-1,0],[0,-1]]

count = 0
while q :
    x,y = q.popleft()
    if li[x][y] == "P" :
        count += 1
    for dx,dy in move :
        if x+dx < n and x+dx >=0 and y+dy < m and y+dy >= 0 and visited[x+dx][y+dy] == 0:
            visited[x+dx][y+dy] = 1
            q.append(((x+dx),(y+dy)))

if count == 0 :
    print("TT")
else :
    print(count)
