"""
Date : 21년 3월 1일
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
input_data = input().split()

x, y = 1, 1

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

s = ['L', 'R', 'U', 'D']
for data in input_data:
    for i in range(len(s)):
        if data == s[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)