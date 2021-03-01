"""
Date : 20년 3월 1일
Description : Algorithm Study
Title : 음료수 얼려 먹기
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

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
result = 0
def dfs(x,y):

    if x <= -1 or x >= n or y <= -1 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
        
print(result)