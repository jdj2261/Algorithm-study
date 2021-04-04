"""
Date : 21. 04. 04
Title : 특정 거리의 도시 찾기
"""

from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([x])
distance[x] = 0

while q:
    cur_node = q.popleft()
    for next_node in graph[cur_node]:
        if distance[next_node] == -1:
            distance[next_node] = distance[cur_node] + 1
            q.append(next_node)

isCity = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i, end = " ")
        isCity = True

if isCity == False:
    print(-1)