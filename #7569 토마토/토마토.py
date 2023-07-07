from collections import deque
n,m,h = map(int, input().split())

li = []
for k in range (h) :
    tmp = []
    for i in range (m) :
        tmp.append(list(map(int,input().split())))
    li.append(tmp)

visited = [[[0 for i in range(n)] for j in range(m)] for k in range(h)]
q = deque()

for k in range(len(li)) :
    for i in range(len(li[0])) :
        for j in range(len(li[0][0])) :
            if li[k][i][j] == 1 :
                q.append((i,j,k, 0))
                visited[k][i][j] = 1
            elif li[k][i][j] == -1 :
                visited[k][i][j] = 1

move = [[1,0,0],[0,1,0],[0,0,1],[-1,0,0],[0,-1,0],[0,0,-1]]

count = 0
while q :
    x,y,z,t = q.popleft()
    count = max(count, t)
    for dx,dy,dz in move :
        if x+dx < m and x+dx >=0 and y+dy < n and y+dy >= 0 and z+dz < h and z+dz >= 0 and visited[z+dz][x+dx][y+dy] == 0:
            visited[z+dz][x+dx][y+dy] = 1
            q.append(((x+dx),(y+dy),(z+dz), t+1))

ans = 0
for k in range(len(li)) :
    for i in range(len(li[0])) :
        for j in range(len(li[0][0])) :
            if visited[k][i][j] == 0 :
                ans = 1
if ans == 1 :
    print(-1)
else :
    print(count)
