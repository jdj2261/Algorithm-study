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

q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while q:
    virus, cur_s, cur_x, cur_y = q.popleft()
    if cur_s == target_s:
        break
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, cur_s + 1, nx, ny))

print(graph[target_x-1][target_y-1])

