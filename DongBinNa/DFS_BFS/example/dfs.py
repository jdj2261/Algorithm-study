"""
Date : 21. 05. 09
Description : DFS 예제
"""

# step 1. 정점, 간선 선언
# step 2. graph -> 인접 행렬 구현
# step 3. 방문 여부 array 선언
# step 4. dfs 함수 구현
# step 5. 결과 출력 

import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
print(graph)
visited = [False] * (n+1)
for i in range(1, m):
    graph[i] = list(map(int, input().split()))

visited = [False] * (n+1)
dfs(graph, 1, visited)