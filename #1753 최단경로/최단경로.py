import sys
import heapq

v, e = map(int, input().split())
start = int(input())
graph = [[] for i in range(v+1)]
q = []
INF = int(10e9)
distance = [INF for i in range(v+1)]

for i in range (e) :
    f, t, cost = map(int, sys.stdin.readline().rstrip().split());
    graph[f].append((t,cost))

def dijkstra(start) :
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        for dest in graph[node] :
            if dist + dest[1] < distance[dest[0]] :
                heapq.heappush(q, (dist + dest[1], dest[0]))
                distance[dest[0]] = dist + dest[1]

dijkstra(start)
for i in range (1, v+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])
