"""
Date : 20년 2월 24일
Description : Algorithm Study
Title : 음료수 얼려 먹기 (DFS) 
"""

"""
N * M
구멍 -> 0
칸막이 -> 1
입력        출력
00110       3
00011
11111
00000
"""

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True :
            result += 2
print(result)