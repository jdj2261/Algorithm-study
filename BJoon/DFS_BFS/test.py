# DFS와 BFS 리뷰
import sys
input = sys.stdin.readline
from collections import deque

# step 1. dfs 구현
# step 2. bfs 구현
'''
n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    visited[v] = True
    q = deque([v])
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in range(1, n+1):
            if not visited[i] and graph[now][i] == 1:
                q.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
'''

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
    # for i in range(1, n+1):
    #     if not visited[i] and graph[v][i] == 1:
    #         dfs(i)

visited = [False] * (n+1)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)