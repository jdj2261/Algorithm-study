"""
Date : 20년 2월 11일
Description : Algorithm Study
Title : 미래도시(최단거리) 
"""
"""
입력 예시    출력 예시
4 2         -1
1 3
2 4
3 4
"""
import sys
input = sys.stdin.readline
INF = int(1e9)
# n : 회사 개수, m : 경로 개수
n, m = map(int, input().split())
graph = [ [INF]*(n+1) for _ in range (n+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)

