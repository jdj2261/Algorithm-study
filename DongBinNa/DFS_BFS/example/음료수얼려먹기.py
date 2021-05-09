"""
Date : 21. 05. 09
Description : DFS 예제
"""

# step 1. graph 정의
# step 2. dfs 구현
# step 3. 결과 출력

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

def dfs(i, j):
    if i < 0  or i >= n or j < 0 or j >= m:
        return False
    if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
