"""
Date : 20년 1월 17일
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
# N : 시험관 크기, K : 바이러스 종류
N, K = map(int, input().split())

graph = []  # 전체 보드 정보를 담는 리스트  
data = []   # 바이러스에 대한 정보를 담는 리스트
for i in range(N):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(N):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, s, x, y = q.popleft()
    # 정확히 S초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))
            
print(graph[target_x-1][target_y-1])

