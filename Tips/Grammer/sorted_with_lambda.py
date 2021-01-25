costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

costs = sorted(costs, key=lambda x: x[0])
print(costs)

N = int(input())

students = []
for i in range(N):
    students.append(input().split())
# 내림차순, 오름차순, 내림차순, 오름차순
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
