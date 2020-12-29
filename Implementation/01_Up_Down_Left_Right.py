"""
Date : 20년 12월 29일
Description : Algorithm Study 예제 4-1
Title : 상하좌우(Implementation) 
"""

"""

입력 예시
5
R R R U D D

출력 예시
3 4
"""

N = int(input("N을 입력하세요 : "))
directions = input("차례대로 입력하세요:").upper().split()

# print(direction)
x, y = 1, 1
nx, ny = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
LRUD = ["L", "R", "U", "D"]

for direction in directions:
    for i in range(len(LRUD)):
        if direction == LRUD[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)

