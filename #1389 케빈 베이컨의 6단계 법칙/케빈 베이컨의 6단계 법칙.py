import heapq

n,m = map(int, input().split())

graph = [[] for i in range(n+1)]
for _ in range(m) :
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

INF = int(1e9)



def dijkstra(start) :
    distance = [INF] * (n+1)
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue

        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    count = 0
    for i in range(1, n+1):
        if distance[i] == INF:
            print("INF")
        else :
            count += distance[i]
    return count
li = []
for i in range(1, n+1) :
    li.append((i,dijkstra(i)))
li.sort(key=lambda x:(x[1], x[0]))
print(li[0][0])




