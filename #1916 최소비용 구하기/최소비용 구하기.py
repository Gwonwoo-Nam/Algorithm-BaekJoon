import heapq
import sys

INF = int(1e9)
n = int(input())
m = int(input())
arr = [[] for i in range(n+1)]

distance = [int(1e9)]*(n+1)
for i in range(m) :
    f, t, cost = map(int, sys.stdin.readline()[:-1].split())
    arr[f].append((t, cost))

def dijkstra(start, end) :
    q=[]
    distance[start] = 0
    heapq.heappush(q, (0, start))
    #print(q)
    # i : 거쳐가는 노드 j : 최종 목적지 노드
    while q:
        dist, node = heapq.heappop(q);
        if (distance[node] < dist) :
            continue
        if node == end :
            continue
        for j in arr[node] :
            if (j[1] + distance[node] < distance[j[0]]) :
                distance[j[0]] = j[1] + distance[node]
                heapq.heappush(q, (distance[j[0]], j[0]))
        #print(q)
    return distance[end]
a,b = map(int, input().split())
print(dijkstra(a,b))
