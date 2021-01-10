"""
너비 우선 탐색 --> queue 이용
일반적으로 DFS보다 BFS 구현이 조금 더 빠르게 동작한다.
"""
from collections import deque

# BFS 메서드 정의
def BFS(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3 ,5],
    [3 ,4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
BFS(graph, 1, visited)