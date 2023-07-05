from collections import deque

n = int(input())
board = []
visited = [[0 for i in range(n)] for j in range(n)]
for i in range(n) :
    board.append(list(map(int,list(input()))))
    for j in range (n) :
        if board[i][j] == 0 :
            visited[i][j] = 1

move = [[1,0], [0,1], [-1, 0], [0 ,-1]]
def dfs(i,j) :
    count = 1
    visited[i][j] = 1
    for dx,dy in move :
        if i+dx >= 0 and i+dx < n and j+dy >= 0 and j+dy < n :
            if visited[i+dx][j+dy] == 0 :
                count += dfs(i+dx, j+dy)
    return count

li = []
for i in range(n) :
    for j in range (n) :
        if visited[i][j] == 0 :
            li.append(dfs(i,j))
li.sort()
print(len(li))
for i in li :
    print(i)
