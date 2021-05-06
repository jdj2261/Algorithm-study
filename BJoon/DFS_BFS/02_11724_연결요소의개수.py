"""
Date : 21. 05. 03
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1 
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1 
2
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())

# dfs
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int ,input().split())
    graph[u][v] = graph[v][u] = 1
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)

# 다른 풀이 (bfs)
from collections import deque
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def bfs(v):
    q = deque([v])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)