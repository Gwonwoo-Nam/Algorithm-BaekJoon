from collections import deque
n = int(input())

arr = []
for i in range (n) :
    arr.append(list(map(int,input().split())))

def dijkstra(node) :
    INF = 0
    route = [INF for i in range(n)]
    visited = [0 for i in range(n)]
    # visited[node] = 1
    q = deque()
    q.append(node)
    while q :
        popped = q.popleft()
        for k in range(n) :
            if arr[popped][k] == 1 and visited[k] == 0:
                route[k] = 1
                q.append(k)
                visited[k] = 1
    return route

for i in range(n) :
    print(" ".join(list(map(str,dijkstra(i)))))