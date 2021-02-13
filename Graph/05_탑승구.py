"""
Date : 21년 2월 13일
Description : Algorithm Study
Title : 탑승구 (그래프 이론) 
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

gate = int(input())
plane = int(input())

parent = [0] * (gate+1)

for i in range(1, gate+1):
    parent[i] = i

result = 0
for _ in range(plane):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data-1)
    result += 1

print(result)