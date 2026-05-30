import sys
input = sys.stdin.readline
import heapq

INF = 1e15
N,M = map(int,input().split())
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v,u,w = map(int,input().split())
    graph[v].append((u,w))


def dstra(start):
    queue = []
    heapq.heappush(queue,(0,start))
    distance[start] = 0

    while queue:
        dist,now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue,(dist + i[1],i[0]))

dstra(1)

for value in distance[2:]:
    if value == INF:
        print(-1)
    else:
        print(value)