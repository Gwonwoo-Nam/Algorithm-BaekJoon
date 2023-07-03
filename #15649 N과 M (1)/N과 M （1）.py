n,m = map(int, input().split())

visited = [0 for i in range(n)]

def dfs(n, m, k) :
  if k < m :
    for i in range(1,n+1) :
      if visited[i-1] == 0 :
        visited[i-1] = 1
        li.append(i)
        dfs(n, m, k+1)
        li.remove(i)
        visited[i-1] = 0
  if k == m :
    print(" ".join(map(str,li)))

li = []
dfs(n, m, 0)