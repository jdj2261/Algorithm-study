"""
Date : 20년 2월 27일
Description : Algorithm Study
Title : 특정 거리의 도시 찾기(BFS) 
"""
"""
도시의 개수 : N, 도로의 개수 : M, 거리 정보 : K, 출발 도시 번호 : X
둘째줄 ~ M개의 줄 : A,B A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재
최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력, 존재하지 않으면 -1 출력
입력예시    출력예시
4 4 2 1     4
1 2
1 3
2 3
2 4
"""
from collections import deque
n, m, k, x = map(int, input().split())
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)