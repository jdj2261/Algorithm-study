"""
Date : 20년 2월 11일
Description : Algorithm Study
Title : 정확한 순위(최단거리) 
"""
"""
입력 예시   출력 예시
6 6         1
1 5
3 4
4 2
4 6
5 2
5 4
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [ [INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# A에서 B로 도달이 가능하거나 B에서 A로 도달이 가능하면 '성적 비교' 가능
result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)