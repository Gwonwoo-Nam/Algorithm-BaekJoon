import sys
sys.setrecursionlimit(10**6)
n = int(input())
li = []

for i in range(n):
    li.append(list(input()))

visited = [[0 for i in range(n)] for j in range(n)]

move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs (x,y, color) :
    visited[x][y] = 1
    for dx, dy in move:
        if x + dx < n and x + dx >= 0 and y + dy < n and y + dy >= 0 and visited[x + dx][y + dy] == 0 :
            if li[x+dx][y+dy] in color :
                dfs(x + dx, y + dy, color)


a = 0
for i in range(len(li)):
    for j in range(len(li[0])):
        if visited[i][j] == 0:
            if li[i][j] in ["R", "G"] :
                a += 1
                dfs(i,j, ["R", "G"])
            else :
                a += 1
                dfs(i,j, ["B"])

visited = [[0 for i in range(n)] for j in range(n)]
b=0
for i in range(len(li)):
    for j in range(len(li[0])):
        if visited[i][j] == 0:
            if li[i][j] in ["R"] :
                b += 1
                dfs(i,j, ["R"])
            elif li[i][j] in ["G"] :
                b += 1
                dfs(i,j, ["G"])
            else :
                b += 1
                dfs(i,j, ["B"])
print(b, a)
