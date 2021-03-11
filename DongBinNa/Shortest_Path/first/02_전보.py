"""
Date : 21년 2월 11일
Description : Algorithm Study
Title : 전보(최단거리) 
"""
"""
입력 예시    출력 예시
3 2 1       2 4
1 2 4
1 3 2
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [ [] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start)) # heap에 (거리, 노드) 넣는다.

    # q가 빌 때까지
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
            
dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드 제외
print(count-1, max_distance)