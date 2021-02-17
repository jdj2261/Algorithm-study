"""
Date : 21년 2월 17일
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
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
