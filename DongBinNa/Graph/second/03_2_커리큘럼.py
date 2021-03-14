"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 커리큘럼 (그래프 이론) 
"""
"""
입력 예시       출력 예시 
5               10
10 -1           20
10 1 -1         14
4 1 -1          18
4 3 1 -1        17
3 3 -1
"""
from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)

graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()