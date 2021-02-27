"""
Date : 20년 2월 27일
Description : Algorithm Study
Title : 연구소 (DFS) 
"""
"""
입력예시            출력예시
4 6                 9
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
"""

n, m = map(int, input().split())

graph = []
temp = [[0]*(m) for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

result = 0
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
                graph[i][j] = 1
                dfs(count)
                count -= 1
                graph[i][j] = 0

dfs(0)
print(result)
