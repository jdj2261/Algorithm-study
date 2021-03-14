"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 팀결성 (그래프 이론) 
"""
"""
1. 팀 합치기 (0 a b)
2. 같은 팀 여부 확인 (1 a b)
입력 예시   출력 예시
7 8         No
0 1 3       No
1 1 7       Yes
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union_parent(parent, b, c)
    elif a == 1:
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")
