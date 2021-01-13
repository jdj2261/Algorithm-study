"""
graph 노드 추가하기

4 4

1 2
1 3
2 3
2 4
[[], [2, 3], [3, 4], [], []]
"""

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)