"""
Date : 20년 2월 27일
Description : Algorithm Study
Title : 경쟁적전염 (BFS) 
"""
"""
입력예시1       출력예시1
3 3             3
1 0 2
0 0 0
3 0 0
2 3 2
"""

from collections import deque

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque(data)

while queue:
    virus, time, x, y = queue.popleft()
    if time == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((virus, time+1, nx, ny))

print(graph[target_x-1][target_y-1])