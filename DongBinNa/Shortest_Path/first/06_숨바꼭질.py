"""
Date : 20년 2월 11일
Description : Algorithm Study
Title : 숨바꼭질(최단거리) 
"""
"""
입력예시    출력예시
6 7         4 2 3
3 6
4 3
3 2
1 3
1 2
2 4
5 2
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [ [] * (n+1) for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

max_node = 0
max_distnace = 0
result = []

for i in range(1, n+1):
    if max_distnace < distance[i]:
        max_node = i
        max_distnace = distance[i]
        result = [max_node]
    elif max_distnace == distance[i]:
        result.append(i)

print(max_node, max_distnace, len(result))