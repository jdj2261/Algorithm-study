"""
Date : 20년 1월 14일
Description : Algorithm Study
Title : 특정거리도시찾기 (BFS) 
"""
"""
입력예시    출력예시
4 4 2 1     4
1 2
1 3
2 3
2 4
"""

from collections import deque
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)

distance = [-1] * (N+1)
distance[X] = 0

q = deque([X])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

print(distance)
check = False 
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)
